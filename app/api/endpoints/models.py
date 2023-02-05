from pydantic import BaseModel

class DataModel(BaseModel):
    """
    Se utiliza para validar de que este llegando una imagen como form-data en el body de la peticion
    """
    image: str
