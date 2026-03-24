from app.core.database import engine
import asyncio
from sqlmodel import SQLModel

async def criar_tabelas() -> None:
    import app.models.__all_models
    
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
        
if __name__=='__main__':
    import asyncio
    asyncio.run(criar_tabelas())