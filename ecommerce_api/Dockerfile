# Imagen base de Python
FROM python:3.10-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        postgresql-client \
        netcat-traditional \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements/base.txt requirements/base.txt
COPY requirements/local.txt requirements/local.txt

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements/local.txt

# Copiar el proyecto
COPY . .

# Copiar y dar permisos al script de entrada
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Puerto
EXPOSE 8000

# Script de entrada
ENTRYPOINT ["/docker-entrypoint.sh"]

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 