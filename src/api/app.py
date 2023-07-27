from fastapi import FastAPI
from .v1.routes import app as api_v1


def init_api_server():
    app = FastAPI()
    app.mount(f'/api/v1', api_v1)
    return app
