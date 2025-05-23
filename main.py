from fastapi import FastAPI, Request, Form

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from core.config import settings
from database.supabase_connection import save_fill_complete
import core.lw_log as lw_log
import github.data_github as github
import avg_chart.chart as chart
from database.conect_database import conect
#from model.utils import map_gender
import joblib
import a_b_testing.model_b as model_a_b
import random
from contextlib import asynccontextmanager

import pandas as pd
from fastapi import Query
#from typing import Optional, List

#from fastapi import status

model_a = joblib.load(settings.model_path_A)
model_b = joblib.load(settings.model_path_B)
class_map = joblib.load(settings.class_map_path)
inv_class_map = {v: k for k, v in class_map.items()}

# uvicorn main:app --reload

VERSION=github.get_latest_github_tag()

@asynccontextmanager
async def lifespan(app: FastAPI):
    model_a_b.load_data()
    yield

#Crear la app
app = FastAPI(
    title=settings.proyect_name,
    description=settings.description,
    version=VERSION
    )
print("\n🚀 Uvicorn escuchando en 0.0.0.0:8000 (dentro del contenedor)")
print("🌐 Accede desde tu navegador en: http://127.0.0.1:8000\n")

#Servir carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")
#Configurar Jinja2 para las plantillas HTML
templates = Jinja2Templates(directory="templates")


# Ruta principal - Renderiza el formulario HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    creators_str = ", ".join(settings.creators)
    year  = datetime.now().year

    github.get_repo_info()
    github.get_repo_contributors()
    lw_log.write_log(f"✅ Acceso a la página principal")
    # Leer todos los registros de la tabla
    response = conect.client.table("body_performance").select("*").order("id", desc=True).execute()
    # Redondear body_fat_percent a entero en cada registro
    if response.data:
        for row in response.data:
            if "body_fat_percent" in row and row["body_fat_percent"] is not None:
                row["body_fat_percent"] = int(round(row["body_fat_percent"]))
    #print("Response:", response.data)
    
    # Cargar los datos 
    return templates.TemplateResponse(request,
        "index.html", 
        {
            "request": request, 
            "title": settings.proyect_name + ", " + VERSION,
            "description": settings.description,
            "slogan": settings.slogan,
            "apipref": settings.api_prefix + settings.api_version,
            "creators": creators_str,
            "date": year,
            "body_performance": response.data,

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
                    gripforce: float = Form(...),
                    sit_bend_cm: float = Form(...),
                    situps: int = Form(...),
                    broad_jump_cm: float = Form(...)
                ):

    try:
        input_data = {
            "age": age,
            "gender": gender,
            "height_cm": height_cm,
            "weight_kg": weight_kg,
            "body_fat_percent": body_fat,
            "diastolic": diastolic,
            "systolic": systolic,
            "gripforce": gripforce,
            "sit_and_bend_forward_cm": sit_bend_cm,
            "sit_ups_counts": situps,
            "broad_jump_cm": broad_jump_cm,
            }
        chart_avg = chart.get_data(gender, age)
        print("Media de salto:", chart_avg)
        lw_log.write_log(f"✅ Recibido datos {input_data}")
        rmd = random.random()
        ver = "A" if rmd < 0.5 else "B"
        model = model_a if ver == "A" else model_b
        lw_log.write_log(f"✅ Modelo seleccionado: {ver}")
        # predicción
        df = pd.DataFrame([input_data])
        pred = model.predict(df)[0]
        proba = model.predict_proba(df).max()
        class_label = inv_class_map[pred]
        # resultados
        result = {
                "prediction": class_label,
                "probability": float(proba)
            }
        # proba = model.predict_proba(df)
        # print("Probabilidades por clase:", proba[0])
        print("Prediction result:", result)
        lw_log.write_log(f"✅ Prediction: {result}")
        # Guardar en la base de datos
        save_fill_complete(input_data, class_label)
        return (result, input_data, chart_avg)
    except Exception as e:
        lw_log.write_log(f"🗑 Error: {e}")
        lw_log.write_log(f"💥Error al procesar los datos {input_data}")

@app.get(settings.api_prefix+settings.api_version+"/logs")

async def logs(request: Request, date: str = Query(None, description="Fecha en formato YYYY-MM-DD")):
    logs = lw_log.read_file_logs(date) if date else lw_log.read_file_logs()
    return logs.strip('"')


