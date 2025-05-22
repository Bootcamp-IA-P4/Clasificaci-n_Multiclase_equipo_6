#import os
#from supabase import create_client, Client
#from dotenv import load_dotenv
import core.lw_log as lw_log
from database.conect_database import conect

#load_dotenv()
# Initialize Supabase client

#supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
# Save data to Supabase
def save_completa(data_dict):
    try:
        response = conect.client.table("body_performance").insert(data_dict).execute()
        print("Fila guardada correctamente en la base de datos (supabase).")
        lw_log.write_log(f"✅ Los datos se han guardado correctamente")
        return response
    except Exception as e:
        lw_log.write_log(f"❌ Parece que ha habido un error con la BBDD: {e}")
        print("Error al guardar en Supabase:", e)
        return None

def save_fill_complete(features: dict, predict):
    try:
        data_dict = {
            "age": features.get("age"),
            "gender": features.get("gender"),
            "height_cm": features.get("height_cm"),
            "weight_kg": features.get("weight_kg"),
            "body_fat_percent": features.get("body_fat_percent"),
            "diastolic": features.get("diastolic"),
            "systolic": features.get("systolic"),
            "gripforce": features.get("gripforce"),
            "sit_and_bend_forward_cm": features.get("sit_and_bend_forward_cm"),
            "sit_ups_counts": features.get("sit_ups_counts"),
            "broad_jump_cm": features.get("broad_jump_cm"),
            "class": predict,
        }
        #print("data_dict:", data_dict)
        save_completa(data_dict)
        #return response
    except Exception as e:
        print("BD Error while saving data:", e)

        return None