from __future__ import annotations
from sqlmodel import Field, SQLModel, ForeignKey, Integer, Relationship
from typing import Optional
from decimal import Decimal
from datetime import datetime


class AgendamentoModel(SQLModel, table=True):
    __tablename__ = 'agendamentos'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    data_hora: datetime
    descricao: Optional[str] = None
    valor: Decimal
    
    cliente_id: int = Field(foreign_key="clientes.id")
    servico_id: int = Field(foreign_key="servicos.id")

    cliente: Optional["ClienteModel"] = Relationship(back_populates="agendamentos")
    servico: Optional["ServicoModel"] = Relationship(back_populates="agendamentos")