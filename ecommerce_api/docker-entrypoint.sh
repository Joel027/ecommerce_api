#!/bin/sh

# Esperar a que la base de datos esté disponible
echo "Esperando a que la base de datos esté disponible..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Base de datos disponible"

# Ejecutar migraciones
echo "Aplicando migraciones..."
python manage.py migrate

# Crear superusuario si no existe
echo "Creando superusuario..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
# Eliminar todos los usuarios existentes
User.objects.all().delete()
# Crear nuevo superusuario
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='Admin123456',
    name='Administrador',
    last_name='Sistema'
)
print("Superusuario creado exitosamente")
END

# Ejecutar el comando pasado a docker
echo "Iniciando servidor..."
exec "$@" 