from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios" #nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    clave = Column(String, nullable=False)

class Autor(Base):
    __tablename__ = "autores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    nacionalidad = Column(String)
    fec_nacimiento = Column(String)
    fec_fallecimiento = Column(String)

class Editorial(Base):
    __tablename__ = "editoriales"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Genero(Base):
    __tablename__ = "generos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Libro(Base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor_id = Column(Integer, ForeignKey("autores.id")) #relación con la tabla autores
    editorial_id = Column(Integer, ForeignKey("editoriales.id"))
    genero_id = Column(Integer, ForeignKey("generos.id"))
    año_publicacion = Column(String)
    cantidad_disponible = Column(Integer)

class Bibliotecario(Base):
    __tablename__ = "bibliotecarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    clave = Column(String, nullable=False)
