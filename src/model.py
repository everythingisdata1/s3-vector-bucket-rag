from pydantic import BaseModel, Field


class S3Vectors(BaseModel):
    key: str
    data: dict = Field(default_factory=dict)
    metadata: dict = Field(default_factory=dict)
