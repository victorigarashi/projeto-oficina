from fastapi import APIRouter, status, Depends, HTTPException, responses
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List
from app.core.deps import get_session
from app.services import cliente_services
from app.schemas.cliente_schemas import ClienteCreate, ClienteResponse, ClienteUpdate
from app.models.cliente_models import ClienteModel


router = APIRouter()
#router criar clientes
@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=ClienteResponse)
async def post_cliente(cliente: ClienteCreate, db: AsyncSession = Depends(get_session)):
    return await cliente_services.criar_cliente(db, cliente)

#router lista clientes
@router.get('/', response_model=List[ClienteResponse])
async def get_clientes(db: AsyncSession = Depends(get_session)):
    return await cliente_services.listar_clientes(db)

#router busca cliente por id 
@router.get('/{cliente_id}', status_code=status.HTTP_200_OK,
            response_model=ClienteResponse)
async def get_cliente_by_id(cliente_id: int, db: AsyncSession = Depends(get_session)):
    cliente = await cliente_services.buscar_cliente(db, cliente_id)
    
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado")
    
    return cliente

#router busca clinete por nome
@router.get('/buscar/', status_code=status.HTTP_200_OK,
            response_model=list[ClienteResponse])
async def get_cliente_by_nome(nome: str, db: AsyncSession = Depends(get_session)):
    cliente = await cliente_services.buscar_cliente_por_nome(db, nome)
    
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado")
    
    return cliente
    
#router atuliza cliente
@router.put('/{cliente_id}', status_code=status.HTTP_200_OK,
            response_model=ClienteUpdate)
async def put_cliente(cliente_id: int, dados: ClienteUpdate, db: AsyncSession = Depends(get_session)):
    cliente = await cliente_services.atualizar_cliente(
        db, cliente_id, dados
    )

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    return cliente

#router delete cliente
@router.delete('/{cliente_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_cliente(cliente_id: int, db: AsyncSession = Depends(get_session)):
    sucesso = await cliente_services.deletar_cliente(db, cliente_id)

    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    return None