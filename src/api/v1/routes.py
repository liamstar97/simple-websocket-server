from fastapi import FastAPI

from .endpoints import websocket_server

app = FastAPI()

app.include_router(
    websocket_server.router,
    prefix='/websocket-server',
    tags=['websocket-server']
)
