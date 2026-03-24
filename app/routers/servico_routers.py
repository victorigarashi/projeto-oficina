from fastapi import APIRouter, status, Depends, HTTPException, responses
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.models.servico_models import ServicoModel
from app.schemas.servico_schemas import ServicoCreate, ServicoResponse, ServicoUpdate
from app.core.deps import get_session
from app.services import servico_services
from typing import List



router = APIRouter()

@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=ServicoResponse)
async def post_servico(servico: ServicoCreate,
                       db: AsyncSession = Depends(get_session)):
    return await servico_services.criar_servico(db, servico)

#lista todos servicos
@router.get('/', response_model=List[ServicoResponse])
async def get_servicos(db: AsyncSession = Depends(get_session)):
    return await servico_services.listar_servicos(db)


#busca servico por id
@router.get('/{servico_id}', 
            response_model=ServicoResponse,
            status_code=status.HTTP_200_OK)
async def get_servico_by_id(servico_id: int, db: AsyncSession = Depends(get_session)):
    servico = await servico_services.buscar_servico(db, servico_id)

    if not servico:
        raise HTTPException(
            status_code=404,
            detail="Serviço não encontrado"
        )

    return servico


#busca servico por nome
@router.get('/buscar/',
            response_model=list[ServicoResponse],
            status_code=status.HTTP_200_OK)
async def get_servico_by_nome(nome: str, db: AsyncSession = Depends(get_session)):
    servico = await servico_services.buscar_por_nome(db, nome)

    if not servico:
        raise HTTPException(
            status_code=404,
            detail="nenhum serviço encontrado"
        )

    return servico

#atualiza servico
@router.put('/{servico_id}',
               response_model=ServicoUpdate,
               status_code=status.HTTP_200_OK)
async def put_servico(servico_id: int, dados:ServicoUpdate, db: AsyncSession = Depends(get_session)):
    
    servico = await servico_services.atualizar_servico(
        db, servico_id, dados
    )

    if not servico:
        raise HTTPException(
            status_code=404,
            detail="Serviço não encontrado"
        )

    return servico


#deleta servico
@router.delete('/{servico_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_servico(servico_id: int,
                         db: AsyncSession = Depends(get_session)):
    sucesso = await servico_services.deletar_servico(db, servico_id)

    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Serviço não encontrado"
        )

    return None