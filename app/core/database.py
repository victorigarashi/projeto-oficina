from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from app.core.configs import settings
from sqlalchemy.orm import sessionmaker


engine: AsyncEngine = create_async_engine(settings.DB_URL)

AsyncSessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)