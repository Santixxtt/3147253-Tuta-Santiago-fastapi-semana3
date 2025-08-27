from pydantic import BaseModel
from typing import Optional

# USUARIOS

class UsuarioBase(BaseModel):  # se pide crear una clase base para los usuarios
    nombre: str
    apellido: str
    correo: str

class UsuarioCreate(UsuarioBase):
    clave: str

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

# Para login (solo se pide correo y clave)
class UsuarioLogin(BaseModel):
    correo: str
    clave: str

