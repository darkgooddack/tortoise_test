from app.repositories import JuiceRepository
from app.schemas import JuiceCreate, JuiceUpdate

class JuiceService:
    @staticmethod
    async def list_juices():
        return await JuiceRepository.get_all()

    @staticmethod
    async def get_juice(juice_id: int):
        return await JuiceRepository.get_by_id(juice_id)

    @staticmethod
    async def create_juice(data: JuiceCreate):
        return await JuiceRepository.create(**data.model_dump())

    @staticmethod
    async def update_juice(juice_id: int, data: JuiceUpdate):
        juice = await JuiceRepository.get_by_id(juice_id)
        if not juice:
            return None
        return await JuiceRepository.update(juice_id, **data.model_dump(exclude_unset=True))

    @staticmethod
    async def delete_juice(juice_id: int):
        await JuiceRepository.delete(juice_id)
