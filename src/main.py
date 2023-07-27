import uvicorn
import os

from fastapi import FastAPI
from api.app import init_api_server

app = FastAPI()


def set_cwd():
    """
    set current working directory to this file's path incase script was ran outside the current directory
    """
    current_file_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_file_path)


def start_api_server():
    # start api server listening for session requests
    app = init_api_server()
    uvicorn.run(app, port=8888)


def main():
    set_cwd()
    start_api_server()


if __name__ == "__main__":
    main()
