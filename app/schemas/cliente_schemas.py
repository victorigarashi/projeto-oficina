from pydantic import EmailStr, Field
from pydantic import BaseModel as ScBaseModel
from  typing import Optional

class ClienteBase(ScBaseModel):
    nome: str = Field(None, min_length=2)
    cpf: str = Field(None, unique=True, min_length=11, max_length=11,)
    email: Optional[EmailStr] = None
    cidade: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass
    
    
class ClienteUpdate(ScBaseModel):
    nome: str = Field(None, min_length=2)
    cpf: str = Field(None, unique=True, min_length=11, max_length=11,)
    email: Optional[EmailStr] = None
    cidade: Optional[str] = None
    
    
class ClienteResponse(ClienteBase):
    id: int
    
    class Config:
        model_config = {"from_attributes": True}