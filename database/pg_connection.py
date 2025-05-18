import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    try:
        conn = psycopg2.connect(
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
            dbname=os.getenv("dbname")
        )
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None