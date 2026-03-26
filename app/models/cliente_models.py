from __future__ import annotations
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from pydantic import EmailStr


class ClienteModel(SQLModel, table=True):
    __tablename__ = 'clientes'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    
    nome: str = Field(min_length=2)
    cpf: str = Field(unique=True, min_length=11, max_length=11,)
    email: Optional[EmailStr] = None
    cidade: Optional[str] = None
    
    
    agendamentos: list["AgendamentoModel"] = Relationship(back_populates="servico")