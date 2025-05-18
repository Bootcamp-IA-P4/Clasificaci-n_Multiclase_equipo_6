# docker compose up --build
# Usar la imagen oficial de Python
# subir imagnes a docker hub
# docker build -t jcmacias/scraping:v1.0 --> nombre del repositorio .  <- importante el punto al final
# docker push jcmacias/scraping:v1.0
# docker run -d -p 8000:8000 jcmacias/scraping:v1.0
ARG PYTHON_VERSION=3.11.11
FROM python:${PYTHON_VERSION}-slim AS builder

#FROM python:3.10.8-slim

# Establecer el directorio de trabajo
# Prevents Python from writing pyc files and keeps Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copiar los archivos del proyecto
#COPY . /app
#instalar dependencias os
USER root

# para evitar errores
RUN mkdir -p /tmp/cache/fontconfig && chmod 777 /tmp/cache/fontconfig
ENV FONTCONFIG_PATH=/tmp/cache/fontconfig




# Instalar dependencias py
RUN python -m pip install --upgrade pip
COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir -r requirements.txt

# Definir variables de entorno 

#ENV LOG_TXT="log.txt"
#ENV LOG_PKL="log.pkl"
#COPY log.txt /app/${LOG_TXT}
  
ENV PYTHONPATH=/app

# Permisos en directorios
RUN mkdir -p /app && \
    chmod -R 777 /app
RUN mkdir -p /var/log

#RUN touch -a ${LOG_TXT}
#RUN chmod 777 ${LOG_TXT}

#RUN touch -a ${LOG_PKL}
#RUN chmod 777 ${LOG_PKL}


COPY . .



# Exponer el puerto 8000
EXPOSE 8000

# ejecutar script sh
#COPY start.sh /start.sh
#RUN chmod +x /start.sh
#CMD ["/start.sh"]
#CMD service cron start && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]