from pydantic import BaseModel, Field, PositiveFloat, PositiveInt, NonNegativeInt
from typing import Optional

class JuiceCreate(BaseModel):
    name: str = Field(..., min_length=1, example="Ананасовый сок")
    price: PositiveFloat = Field(..., example=100.0)
    quantity: NonNegativeInt = Field(..., example=50)
    supplier_id: PositiveInt = Field(..., example=1)

class JuiceUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, example="Апельсиновый сок")
    price: Optional[PositiveFloat] = Field(None, example=120.0)
    quantity: Optional[NonNegativeInt] = Field(None, example=30)
    supplier_id: Optional[PositiveInt] = Field(None, example=2)

class JuiceOut(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    supplier_id: int

    class Config:
        from_attributes = True
