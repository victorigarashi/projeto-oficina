from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import AsyncSessionLocal
from typing import AsyncGenerator

async def get_session()  -> AsyncGenerator:
    session: AsyncSession = AsyncSessionLocal()
    
    try:
        yield session
    finally:
        await session.close()