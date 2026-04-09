from pydantic import BaseModel, EmailStr
from typing import Optional

class Estudiante(BaseModel):
    carnet: str
    nombre: str
    correo: EmailStr
    telefono: str
