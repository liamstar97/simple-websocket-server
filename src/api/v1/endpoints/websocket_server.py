from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from api.api_resources import WebSocketConnectionManager  # type: ignore

router = APIRouter()

websocket_manager = WebSocketConnectionManager()


@router.websocket('')
async def logger_websocket(websocket: WebSocket):
    await websocket_manager.connect(websocket)
    try:
        while True:
            message = await websocket.receive_json()
            await websocket_manager.broadcast(message)
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)


@router.get('/hello_world')
async def hello_world(request: Request):
    return {"hello": "world!"}
