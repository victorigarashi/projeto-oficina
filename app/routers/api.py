from app.routers import servico_routers, cliente_routers, agendamentos_routers
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(servico_routers.router, prefix='/servicos', tags=['servicos'])
api_router.include_router(cliente_routers.router, prefix='/clientes', tags=['clientes'])
api_router.include_router(agendamentos_routers.router, prefix='/agendamentos', tags=['agendamentos'])