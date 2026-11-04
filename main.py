from src.s3vector_oprations import query_embedding, add_embedding

if __name__ == "__main__":
    # Ingestion
    add_embedding()

    # Retrieval
    query = "Does Bharat have any AI certifications?"

    results = query_embedding(query)
