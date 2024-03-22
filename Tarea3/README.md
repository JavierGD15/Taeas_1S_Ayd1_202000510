# Despliegue de la Aplicación Flask en Docker

Este documento describe los pasos necesarios para desplegar una aplicación Flask utilizando Docker en un entorno local. La aplicación Flask expone un endpoint que devuelve información específica cuando se accede a través de una petición GET.

## Prerrequisitos

Asegúrate de tener Docker instalado en tu máquina local. Puedes descargarlo e instalarlo desde [Docker Hub](https://hub.docker.com/).

## Estructura del Proyecto

El proyecto consta de los siguientes archivos:

- `app.py`: Archivo de Python que contiene la lógica del servidor Flask.
- `requirements.txt`: Archivo que lista las dependencias necesarias para la aplicación Flask.
- `Dockerfile`: Archivo de Docker que contiene las instrucciones para construir la imagen del contenedor.

## Construcción de la Imagen Docker

Para construir la imagen Docker de tu aplicación, navega al directorio que contiene tu `Dockerfile` y ejecuta el siguiente comando:

```bash
docker build -t flask-app .
```
Este comando inicia un contenedor de Docker que ejecuta la aplicación Flask, mapeando el puerto 5000 del contenedor al puerto 5000 de tu máquina local.

## Llamada de la petición GET

Para probar el endpoint de la API, puedes hacer una petición GET. Esto se puede hacer usando una herramienta como `curl` o simplemente a través de tu navegador web.

### Usando `curl`

Ejecuta el siguiente comando en tu terminal:

curl http://localhost:5000/


### Usando un navegador web

Abre tu navegador y navega a `http://localhost:5000/`.

## Respuesta esperada

202000510 ANALISIS Y DISEÑO DE SISTEMAS 1 Sección B Bryan Páez

Esta respuesta indica que el servidor está corriendo correctamente dentro del contenedor Docker y que el endpoint está respondiendo como se espera.
