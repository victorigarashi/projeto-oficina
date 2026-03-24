from typing import List, ClassVar
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://user:12345@localhost:5432/projeto_oficina'
    
    class Config:
        case_sensitive = True

            

settings: Settings  = Settings()