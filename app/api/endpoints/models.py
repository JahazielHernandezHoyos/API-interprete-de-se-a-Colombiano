from pydantic import BaseModel

class DataModel(BaseModel):
    """
    Data model for processing images
    """
    data: str
