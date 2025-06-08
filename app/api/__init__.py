from fastapi import APIRouter
from app.api.juice import router as juice_router

api_router = APIRouter()
api_router.include_router(juice_router)
