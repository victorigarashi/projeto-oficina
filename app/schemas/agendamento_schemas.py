from typing import Optional
from pydantic import BaseModel as ScBaseModel
from datetime import datetime
from decimal import Decimal
from pydantic import Field, ConfigDict
from app.schemas.cliente_schemas import ClienteBase
from app.schemas.servico_schemas import ServicoBase


class AgendamentoBase(ScBaseModel):
    data_hora: datetime
    descricao: Optional[str] = None
    valor: Decimal
    
    
    cliente_id: int
    servico_id: int
    
    
class AgendamentoCreate(AgendamentoBase):
    pass


class AgendamentoUpdate(AgendamentoBase):
    data_hora: Optional[datetime] = None
    descricao: Optional[str] = None
    valor: Optional[Decimal] = None

class AgendamentoResponse(ScBaseModel):
    id: int
    status: str
    
    cliente: ClienteBase
    servico: ServicoBase
    
    model_config = ConfigDict(from_attributes=True)