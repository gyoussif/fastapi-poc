import logging

from fastapi import FastAPI

from src.database import engine

from . import models, routers
from .logger import RouterLoggingMiddleware

models.Base.metadata.create_all(bind=engine)


def get_app() -> FastAPI:

    return FastAPI(title="FastAPI poc", debug=True)


app = get_app()
app.add_middleware(
    RouterLoggingMiddleware,
    logger=logging.getLogger(__name__)
)

app.include_router(routers.cart_router)
