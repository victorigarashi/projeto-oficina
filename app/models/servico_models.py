from __future__ import annotations
from sqlmodel import Field, SQLModel, Relationship
from decimal import Decimal
from typing import Optional




class ServicoModel(SQLModel, table=True):
    __tablename__ = 'servicos'
    
    id: Optional[int] = Field(default=None, primary_key=True)

    nome_servico: str = Field(index=True)
    valor: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    descricao: str
    ativo: bool = Field(default=True)
    tempo_estimado: int = Field(gt=0)
    categoria: Optional[str] = Field(default=None)
    codigo: Optional[str] = Field(default=None, index=True, unique=True)
    
    agendamentos: list["AgendamentoModel"] = Relationship(back_populates="servico")