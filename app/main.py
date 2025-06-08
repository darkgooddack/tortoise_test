from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api import api_router

app = FastAPI()
app.include_router(api_router)

TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:pass1234@localhost:5432/juice",
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # миграции управляются Aerich
    add_exception_handlers=True,
)
