from fastapi import APIRouter, HTTPException
from app.services import JuiceService
from app.schemas.juice import JuiceCreate, JuiceUpdate, JuiceOut
from typing import List

router = APIRouter(prefix="/juices", tags=["Juices"])

@router.get("/", response_model=List[JuiceOut])
async def list_juices():
    return await JuiceService.list_juices()

@router.get("/{juice_id}", response_model=JuiceOut)
async def get_juice(juice_id: int):
    juice = await JuiceService.get_juice(juice_id)
    if not juice:
        raise HTTPException(status_code=404, detail="Сок не найден")
    return juice

@router.post("/", response_model=JuiceOut)
async def create_juice(data: JuiceCreate):
    return await JuiceService.create_juice(data)

@router.put("/{juice_id}", response_model=JuiceOut)
async def update_juice(juice_id: int, data: JuiceUpdate):
    updated = await JuiceService.update_juice(juice_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Сок не найден")
    return updated

@router.delete("/{juice_id}")
async def delete_juice(juice_id: int):
    await JuiceService.delete_juice(juice_id)
    return {"detail": "Сок удалён"}
