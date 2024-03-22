# Usar una imagen base de Python
FROM python:3.8-slim-buster

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios para la aplicación
COPY app.py /app
COPY requirements.txt /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Definir el comando para ejecutar la aplicación
CMD ["python", "app.py"]