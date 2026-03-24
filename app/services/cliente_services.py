from app.models.cliente_models import ClienteModel
from app.schemas.cliente_schemas import ClienteCreate, ClienteUpdate
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession


#criar clientes
async def criar_cliente(db: AsyncSession, novo_cliente: ClienteCreate):
    db_cliente = ClienteModel(**novo_cliente.model_dump())

    db.add(db_cliente)
    await db.commit()
    await db.refresh(db_cliente)

    return db_cliente

#lista todos os clientes
async def listar_clientes(db: AsyncSession):
    result = await db.execute(select(ClienteModel))
    return result.scalars().all()

#busca cliente por id 
async def buscar_cliente(db: AsyncSession, cliente_id: int):
    result = await db.get(ClienteModel, cliente_id)
    return result

#busca cliente por nome
async def buscar_cliente_por_nome(db: AsyncSession, nome: str):
    query = select(ClienteModel).where(
        ClienteModel.nome.ilike(f"%{nome}%")
    )

    result = await db.execute(query)
    return result.scalars().all()
 
 #atualiza cliente
async def atualizar_cliente(db: AsyncSession, servico_id: int, dados: ClienteUpdate):
    cliente = await db.get(ClienteModel, servico_id)

    if not cliente:
        return None

    update_data = dados.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(cliente, key, value)

    db.add(cliente)
    await db.commit()
    await db.refresh(cliente)

    return cliente

#deleta cliente
async def deletar_cliente(db: AsyncSession, cliente_id: int):
    cliente = await db.get(ClienteModel, cliente_id)

    if not cliente:
        return False

    await db.delete(cliente)
    await db.commit()

    return True