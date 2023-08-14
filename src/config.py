import os

from dotenv import load_dotenv

load_dotenv()
ENV_STATE = os.getenv("ENV_STATE", default='dev')
HOST = os.getenv("HOST", default='127.0.0.1')
PORT = os.getenv("PORT", default='8000')
