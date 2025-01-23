import uvicorn
from fastapi import FastAPI

class API:
    def __init__(self, host: str, port: int):
        self.app = FastAPI()

