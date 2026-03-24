from sqlmodel import Field, SQLModel
from typing import Optional
from pydantic import EmailStr

class ClienteModel(SQLModel, table=True):
    __tablename__: str ='clientes'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    nome: str = Field(None, min_length=2)
    cpf: str = Field(None, unique=True, min_length=11, max_length=11,)
    email: Optional[EmailStr] = None
    cidade: Optional[str] = None