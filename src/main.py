from fastapi import FastAPI
from .logger import RouterLoggingMiddleware
from src.database import engine
import logging
from . import models,routers

models.Base.metadata.create_all(bind=engine)


def get_app() -> FastAPI:

    return FastAPI(title="FastAPI poc", debug=True)


app = get_app()
app.add_middleware(
    RouterLoggingMiddleware,
    logger=logging.getLogger(__name__)
)

app.include_router(routers.cart_router)
