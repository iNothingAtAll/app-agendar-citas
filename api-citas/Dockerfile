# Imagen base
FROM python:3.11.0-alpine3.15


# Establece el directorio de trabajo
WORKDIR /app


COPY . .


# Instala las dependencias
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt


# Expone el puerto por defecto de Flask
EXPOSE 5001


# Variables de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development


# Comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
