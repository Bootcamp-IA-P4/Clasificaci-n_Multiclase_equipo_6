from fastapi import FastAPI, Request, Form

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from core.config import settings
from database.supabase_connection import save_fill_complete


import pandas as pd
from typing import Optional, List

from fastapi import status



# uvicorn main:app --reload



#Crear la app
app = FastAPI(
    title=settings.proyect_name,
    description=settings.description,
    version=settings.version
    )


#Servir carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")
#Configurar Jinja2 para las plantillas HTML
templates = Jinja2Templates(directory="templates")


# Ruta principal - Renderiza el formulario HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    creators_str = ", ".join(settings.creators)
    year  = datetime.now().year
    # Cargar los datos de prueba desde el archivo CSV
    return templates.TemplateResponse(request,
        "index.html", 
        {
            "request": request, 
            "title": settings.proyect_name + ", " + settings.version,
            "description": settings.description,
            "apipref": settings.api_prefix + settings.api_version,
            "creators": creators_str,
            "date": year,
            "body_performance": settings.datos_prueba,
        }
    )


# Endpoint para la predicción multiple
@app.post(settings.api_prefix+settings.api_version+"/predict")
async def predict(
    age: float = Form(...),
    gender: str = Form(...),
    height_cm: float = Form(...),
    weight_kg: float = Form(...),
    body_fat: float = Form(...),
    diastolic: float = Form(...),
    systolic: float = Form(...),
    gripForce: float = Form(...),
    sit_bend_cm: float = Form(...),
    situps: int = Form(...),
    broad_jump_cm: float = Form(...)
):
    


    input_data = {
        "age": age,
        "gender": gender,
        "height_cm": height_cm,
        "weight_kg": weight_kg,
        "body_fat_%": body_fat,
        "diastolic": diastolic,
        "systolic": systolic,
        "gripForce": gripForce,
        "sit_and_bend_forward_cm": sit_bend_cm,
        "sit-ups_counts": situps,
        "broad_jump_cm": broad_jump_cm,
    }
    
    print("Received data:", input_data)
    save_fill_complete(input_data)
    return JSONResponse(input_data)