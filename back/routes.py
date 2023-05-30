from fastapi import APIRouter, HTTPException

from schemas import Converter
from utils import Utils

component_router = APIRouter(prefix="/componente")
utils_router = APIRouter(prefix="/utils")

# Agregar rutas al componente_router
@utils_router.post("/convert/")
async def convertir_md_csv(input: Converter):
    try:
        csv = Utils.md_to_csv(input.ruta_md+input.nombre+".md",
                              input.ruta_csv+input.nombre+".csv")
        return {"mensaje": "conversión exitosa!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor : {e}")

@utils_router.post("/preparar")
async def preparar_csv(input: Converter):
    try:
        csv = Utils.md_to_csv(input.ruta_md+input.nombre+".md",
                              input.ruta_csv+input.nombre+".csv")
        return {"mensaje": "conversión exitosa!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor : {e}")
