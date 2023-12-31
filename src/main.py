import logging

from fastapi import FastAPI

from src.database import engine

from . import config, models, routers
from .logger import RouterLoggingMiddleware

models.Base.metadata.create_all(bind=engine)


def get_app() -> FastAPI:

    return FastAPI(title="FastAPI poc", host=config.HOST,
                   port=config.PORT, debug=config.ENV_STATE != "prod")


app = get_app()
app.add_middleware(
    RouterLoggingMiddleware,
    logger=logging.getLogger(__name__)
)

app.include_router(routers.cart_router)
