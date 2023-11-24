# Determina la versión de python necesaria para crear el contenedor
FROM python:3.9

# Establecer directorio de trabajo en app
WORKDIR /app

# Copiar requirements.txt
COPY requirements.txt ./

# Instalar entorno de requirements.txt en contenedor
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Actualizar sistema que está en linux
RUN apt-get update


