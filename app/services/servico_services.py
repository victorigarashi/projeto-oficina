from app.models.servico_models import ServicoModel
from app.schemas.servico_schemas import ServicoCreate
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.servico_schemas import ServicoUpdate


#cria servicos
async def criar_servico(db: AsyncSession, novo_servico: ServicoCreate):
    db_servico = ServicoModel(**novo_servico.model_dump())

    db.add(db_servico)
    await db.commit()
    await db.refresh(db_servico)

    return db_servico



#lista todos os servicos
async def listar_servicos(db: AsyncSession):
    result = await db.execute(select(ServicoModel))
    return result.scalars().all()

#busca servico por id
async def buscar_servico(db: AsyncSession, servico_id: int):
    result = await db.get(ServicoModel, servico_id)
    return result



#busca servico por nome
async def buscar_por_nome(db: AsyncSession, nome: str):
    query = select(ServicoModel).where(
        ServicoModel.nome_servico.ilike(f"%{nome}%")
    )

    result = await db.execute(query)
    return result.scalars().all()



#atualiza servico
async def atualizar_servico(db: AsyncSession, servico_id: int, dados: ServicoUpdate):
    servico = await db.get(ServicoModel, servico_id)

    if not servico:
        return None

    update_data = dados.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(servico, key, value)

    db.add(servico)
    await db.commit()
    await db.refresh(servico)

    return servico


#deleta servico
async def deletar_servico(db: AsyncSession, servico_id: int):
    servico = await db.get(ServicoModel, servico_id)

    if not servico:
        return False

    await db.delete(servico)
    await db.commit()

    return True