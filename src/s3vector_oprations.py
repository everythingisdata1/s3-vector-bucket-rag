import json
import os

from dotenv import load_dotenv

from src.clients import SEP, s3vectors_client, embedd_client
from src.doc_loader import load_docs
from src.embedding import generate_embeddings

load_dotenv(override=True)


def add_embedding():
    print(SEP * 2)
    print("Saving vectors to S3 Vectors...")
    docs = load_docs()
    vectors = generate_embeddings(docs)
    client_obj = s3vectors_client()

    payload = [
        vector.model_dump()
        for vector in vectors
    ]

    response = client_obj.put_vectors(
        vectorBucketName=os.getenv("S3VECTORS_BUCKET"),
        indexName=os.getenv("S3VECTORS_INDEX"),
        vectors=payload
    )

    print("Vector ingestion completed successfully!")

    return response


def query_embedding(query):
    print(SEP * 2)
    print("Fetch vector data.....")

    embedding_client = embedd_client()
    query_vector = embedding_client.embed_query(query.strip())

    client_obj = s3vectors_client()

    response = client_obj.query_vectors(
        vectorBucketName=os.getenv("S3VECTORS_BUCKET"),
        indexName=os.getenv("S3VECTORS_INDEX"),
        queryVector={"float32": query_vector},
        topK=3,
        returnDistance=True,
        returnMetadata=True
    )

    print("Vector search completed successfully!")
    print(json.dumps(response["vectors"], indent=2))
    # for result in response.get("vectors", []):
    #     print(result)

    return response


