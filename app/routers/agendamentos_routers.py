from fastapi import APIRouter, status, Depends, HTTPException, responses
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List
from app.core.deps import get_session
from app.services import agendamentos_services
from app.schemas.agendamento_schemas import AgendamentoCreate, AgendamentoResponse, AgendamentoUpdate
from app.models.agendamento_models import AgendamentoModel


router = APIRouter()

#post
@router.post('/', response_model=AgendamentoResponse, status_code=status.HTTP_201_CREATED)
async def post_agendamentos(agendamento: AgendamentoCreate, db: AsyncSession =  Depends(get_session)):
    return await agendamentos_services.criar_agendamento(db, agendamento)

#get lista todos agendamnetos existentes
@router.get('/', response_model=list[AgendamentoResponse])
async def get_agendamento(db: AsyncSession = Depends(get_session)):
    return await agendamentos_services.listar_agendamentos(db)

#get busca agendamento por id
@router.get('/{agendamento_id}', response_model=AgendamentoResponse, status_code=status.HTTP_200_OK)
async def get_agendamneto_by_id(agendamento_id: int, db: AsyncSession = Depends(get_session)):
    agendamento = await agendamentos_services.buscar_agendamento(db, agendamento_id)
    
    if not agendamento:
        raise HTTPException(
            status_code=404,
            detail="Agendamento não encontrado")
     
    return agendamento

#get lista todos os servico do cliente
@router.get('/buscar/', response_model=list[AgendamentoResponse], status_code=status.HTTP_200_OK)
async def get_agendamento_by_nome(cliente_id: int,nome: str, db: AsyncSession = Depends(get_session)):
    agendamentos = await agendamentos_services.get_agendamentos_by_cliente(db, cliente_id)
    return agendamentos



#put atuliza agendamentos
@router.put('/{agendamento_id}', status_code=status.HTTP_200_OK,
            response_model=AgendamentoUpdate)
async def put_agendamento(agendamento_id: int, dados: AgendamentoUpdate, db: AsyncSession = Depends(get_session)):
    agendamento = await agendamentos_services.atualizar_agendamneto(
        db, agendamento_id, dados
    )

    if not agendamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )

    return agendamento

#delete deleta agendamento
@router.delete('/{agendamento_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_agendamento(agendamento_id: int, db: AsyncSession = Depends(get_session)):
    sucesso = await agendamentos_services.deletar_agendamento(db, agendamento_id)

    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )

    return None