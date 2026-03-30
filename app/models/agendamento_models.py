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
