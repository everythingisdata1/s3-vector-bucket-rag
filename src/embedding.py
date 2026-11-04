from dotenv import load_dotenv

from src.clients import embedd_client
from src.model import S3Vectors

load_dotenv(override=True)


def generate_embeddings(docs):
    print("Generating embeddings...")

    if not docs:
        raise ValueError("No documents found")

    embedding_client = embedd_client()
    embeddings = embedding_client.embed_documents(docs)

    data_vectors = []
    for i, (doc, embedding) in enumerate(zip(docs, embeddings)):
        vector = S3Vectors(
            key=f"bank-report-{i}",
            data={"float32": embedding},
            metadata={
                "source": f"finance-report-{i}",
                "data_type": "bank",
                "content_preview": doc[:100]
            }
        )
        data_vectors.append(vector)

    print(f"Generated vectors: {len(data_vectors)}")

    return data_vectors
