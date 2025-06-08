from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api import api_router

app = FastAPI()

app.include_router(api_router)

register_tortoise(
    app,
    db_url="postgres://postgres:pass1234@localhost:5432/juice",
    modules={"models": ["app.core.models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)