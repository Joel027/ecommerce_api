# E-commerce API

API REST para una plataforma de comercio electrónico desarrollada con Django REST Framework.

## Requisitos

- Python 3.8+
- PostgreSQL
- Virtualenv

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd ecommerce_api
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv_code
source venv_code/bin/activate  # Linux/Mac
venv_code\Scripts\activate  # Windows
```

3. Instalar dependencias:
```bash
# Para desarrollo
pip install -r requirements/local.txt

# Para producción
pip install -r requirements/production.txt
```

4. Configurar variables de entorno:
- Crear archivo `.env` basado en `.env.example`
- Configurar las variables necesarias

5. Ejecutar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Ejecutar servidor de desarrollo:
```bash
python manage.py runserver
```

## Estructura del Proyecto

```
ecommerce_api/
├── apps/               # Aplicaciones del proyecto
│   └── users/         # App de usuarios
├── docs/              # Documentación
├── ecommerce_api/     # Configuración del proyecto
│   └── settings/     # Configuraciones por entorno
├── requirements/      # Requirements por entorno
└── static/           # Archivos estáticos
```

## Desarrollo

- Usar `requirements/local.txt` para dependencias de desarrollo
- Seguir PEP 8 para estilo de código
- Documentar nuevas funcionalidades

## Producción

- Usar `requirements/production.txt`
- Configurar variables de entorno
- Usar gunicorn como servidor WSGI 