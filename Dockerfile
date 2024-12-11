# """
# Dockerfile

# Este archivo define cómo construir la imagen de Docker para el entorno de desarrollo del proyecto Mini Cámara Retro.

# Descripción:
# - Usa una base de Python 3.9 slim.
# - Configura el entorno con las dependencias necesarias para ejecutar la aplicación.
# - Copia los archivos del proyecto al contenedor.
# - Establece el comando principal para ejecutar la aplicación.

# Instrucciones:
# - Construir la imagen: docker-compose build
# - Ejecutar el contenedor: docker-compose up
# """

FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requisitos
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto al contenedor
COPY . .

# Definir el comando por defecto para el contenedor
CMD ["python3", "src/main.py"]
