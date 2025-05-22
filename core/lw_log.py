import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.getcwd()
LOG_PATH = os.path.join(BASE_DIR,  os.getenv("LOG_TXT", "logs.log"))

def read_file_logs(date_filter=None):
    """
    Lee el archivo de logs y retorna las líneas que coinciden con la fecha dada (YYYY-MM-DD).
    Si date_filter es None, retorna todas las líneas.
    """
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        if date_filter:
            # Filtra líneas que contienen la fecha en formato YYYY-MM-DD
            lineas = [line for line in lineas if line.startswith(f"[{date_filter}")]
        contenido_invertido = "<br>".join(line.strip() for line in lineas[::-1])
        return contenido_invertido
    except FileNotFoundError:
        return "Error: Archivo no encontrado\n"
    except Exception as e:
        return f"Error: {e}"
    
def write_log(text):
    with open(LOG_PATH, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {text}\n")