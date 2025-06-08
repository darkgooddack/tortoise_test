from app.models.juice import Juice

class JuiceRepository:
    @staticmethod
    async def get_all():
        return await Juice.all()

    @staticmethod
    async def get_by_id(juice_id: int):
        return await Juice.get_or_none(id=juice_id)

    @staticmethod
    async def create(**kwargs):
        return await Juice.create(**kwargs)

    @staticmethod
    async def update(juice_id: int, **kwargs):
        await Juice.filter(id=juice_id).update(**kwargs)
        return await Juice.get(id=juice_id)

    @staticmethod
    async def delete(juice_id: int):
        await Juice.filter(id=juice_id).delete()
