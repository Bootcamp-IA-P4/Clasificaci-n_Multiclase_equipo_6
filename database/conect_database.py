
import os
from supabase import create_client, Client
from dotenv import load_dotenv
import core.lw_log as lw_log

class SupabaseConexion:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.client = None
        self.conect()

    def conect(self):
        try:
            self.client: Client = create_client(self.url, self.key)
            print("✅ Conexión a Supabase exitosa.")
        except Exception as e:
            print(f"❌ Error al conectar con Supabase: {e}")
            self.client = None

conect = SupabaseConexion()