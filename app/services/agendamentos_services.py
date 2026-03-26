from app.models.agendamento_models import AgendamentoModel
from app.schemas.agendamento_schemas import AgendamentoCreate, AgendamentoUpdate
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


#cria novos agendamentos
async def criar_agendamento(db: AsyncSession, novo_agendamento: AgendamentoCreate):
    db_agendamento = AgendamentoModel(**novo_agendamento.model_dump())

    db.add(db_agendamento)
    await db.commit()
    await db.refresh(db_agendamento)

    return db_agendamento

#lista todos os agendamnentos
async def listar_agendamentos(db: AsyncSession):
    result = await db.execute(select(AgendamentoModel))
    return result.scalars().all()

#agendamento por id
async def buscar_agendamento(db: AsyncSession, agendamento_id: int):
    result = await db.get(AgendamentoModel, agendamento_id)
    return result

#busca todos agendamentos de um cliente
async def get_agendamentos_by_cliente(db: AsyncSession, cliente_id: int):
    statement = (
        select(AgendamentoModel)
        .where(AgendamentoModel.cliente_id == cliente_id)
        .options(
            selectinload(AgendamentoModel.cliente),
            selectinload(AgendamentoModel.servico),
        )
    )

    result = await db.exec(statement)
    return result.all()

#atualiza agendamnetos
async def atualizar_agendamneto(db: AsyncSession, servico_id: int, dados: AgendamentoUpdate):
    agendamento = await db.get(AgendamentoModel, servico_id)

    if not agendamento:
        return None

    update_data = dados.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(agendamento, key, value)

    db.add(agendamento)
    await db.commit()
    await db.refresh(agendamento)

    return agendamento

#deleta agendamentos
async def deletar_agendamento(db: AsyncSession, agendamento_id: int):
    agendamento = await db.get(AgendamentoModel, agendamento_id)

    if not agendamento:
        return False

    await db.delete(agendamento)
    await db.commit()

    return True