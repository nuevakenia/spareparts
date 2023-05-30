
from typing import Optional
from pydantic import BaseModel

class Sistema(BaseModel):
    nombre : str

class Tipo(BaseModel):
    nombre : str

class Componente(BaseModel):
    nombre: str
    Tipo : Tipo
    Sistema : Sistema


class Converter(BaseModel):
    nombre : str
    ruta_md : Optional[str] = None
    ruta_csv : Optional[str] = None


