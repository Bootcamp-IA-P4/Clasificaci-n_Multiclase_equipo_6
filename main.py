from fastapi import FastAPI, Request, Form

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from core.config import settings
from database.supabase_connection import save_fill_complete
import core.lw_log as lw_log
import github.data_github as github
#from model.utils import map_gender
import joblib

import pandas as pd
#from typing import Optional, List

#from fastapi import status

model = joblib.load(settings.model_path_A)
class_map = joblib.load(settings.class_map_path)
inv_class_map = {v: k for k, v in class_map.items()}

# uvicorn main:app --reload



#Crear la app
app = FastAPI(
    title=settings.proyect_name,
    description=settings.description,
    version=settings.version
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
    load_logs = lw_log.read_file_logs()
    github.get_repo_info()
    github.get_repo_contributors()
    lw_log.write_log(f"✅ Acceso a la página principal")
    # Cargar los datos de prueba desde el archivo CSV
    return templates.TemplateResponse(request,
        "index.html", 
        {
            "request": request, 
            "title": settings.proyect_name + ", " + github.get_latest_github_tag(),
            "description": settings.description,
            "apipref": settings.api_prefix + settings.api_version,
            "creators": creators_str,
            "date": year,
            "body_performance": settings.datos_prueba,
            "load_logs": load_logs,
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

    try:
        input_data = {
        "age": age,
        "gender": gender,
        "height_cm": height_cm,
        "weight_kg": weight_kg,
        "body_fat_percent": body_fat,
        "diastolic": diastolic,
        "systolic": systolic,
        "gripforce": gripForce,
        "sit_and_bend_forward_cm": sit_bend_cm,
        "sit_ups_counts": situps,
        "broad_jump_cm": broad_jump_cm,
        }
        lw_log.write_log(f"✅ Recibido datos {input_data}")
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
        print("Prediction result:", result)
        lw_log.write_log(f"✅ Prediction: {result}")
        # Guardar en la base de datos
        save_fill_complete(input_data, class_label)
        return JSONResponse(result)
    except Exception as e:
        lw_log.write_log(f"💥Error al procesar los datos {input_data}")
