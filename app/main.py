from fastapi import FastAPI
from app.routers.api import api_router 
import uvicorn

app = FastAPI(
    title="Sistema de Agendamento - Oficina",
    version="1.0.0",
    description="API para gerenciamento de serviços e veículos"
)

app.include_router(api_router)

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "API rodando com sucesso!", "status": "online"}

if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)