import os

import boto3
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv(override=True)

SEP = "=" * 20

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

if not ACCESS_KEY or not SECRET_KEY:
    raise ValueError("AWS credentials are missing")

session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=AWS_REGION
)


def s3vectors_client():
    print(SEP + " S3-VECTOR-CLIENT " + SEP)
    return session.client("s3vectors")


def bedrock_client():
    print(SEP + " BEDROCK-CLIENT " + SEP)
    return session.client("bedrock-runtime")


def embedd_client():
    print(SEP + " OPENAI-EMBEDDING " + SEP)

    return OpenAIEmbeddings(model="text-embedding-3-small", dimensions=500)
