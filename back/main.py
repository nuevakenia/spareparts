from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from routes import component_router, utils_router
from schemas import Componente,Converter
from utils import Utils

app = FastAPI()
app.include_router(component_router)
app.include_router(utils_router)

@app.post("/get")
async def create_componente(input: Componente):
    return input

