# Usar la imagen oficial de Python 3.10
FROM python:3.10

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . .

# Exponer el puerto 8000
EXPOSE 8000

# # Comando por defecto al ejecutar el contenedor
#RUN uvicorn app:app --reload --host 0.0.0.0 --port 8000
