from pydantic import BaseModel as ScBaseModel
from pydantic import Field
from decimal import Decimal
from typing import Optional

class ServicoBase(ScBaseModel):
    nome_servico: str = Field(..., min_length=2)
    valor: Decimal = Field(..., gt=0)
    descricao: str = Field(..., min_length=3)
    ativo: bool = True
    tempo_estimado: int = Field(..., gt=0)
    categoria: Optional[str] =  Field(None, min_length=2)
    codigo: Optional[str] =  Field(None, min_length=1)
    

class ServicoCreate(ServicoBase):
    pass



class ServicoUpdate(ScBaseModel):
    nome_servico: Optional[str] = Field(None, min_length=2)
    valor: Optional[Decimal] = Field(None, gt=0)
    descricao: Optional[str] = Field(None, min_length=3)
    ativo: Optional[bool] = None
    tempo_estimado: Optional[int] = Field(None, gt=0)
    categoria: Optional[str] =  Field(None, min_length=2)
    codigo: Optional[str] =  Field(None, min_length=1)


class ServicoResponse(ServicoBase):
    id: int
    nome_servico: str
    valor: Decimal
    descricao: str
    ativo: bool
    tempo_estimado: int
    categoria: Optional[str]
    codigo: Optional[str]

    
    class Config:
        model_config = {"from_attributes": True}