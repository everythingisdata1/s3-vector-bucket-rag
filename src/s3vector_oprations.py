from src.clients import create_s3vectors_client
from src.embedding import generate_embeddings


def add_embedding():
    print(SEP * 2)
    print("Saving vectors to S3 Vectors...")

    vectors = generate_embeddings()
    client_obj = create_s3vectors_client()

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


if __name__ == '__main__':
    resp = add_embedding()
    print(resp)
