import os
import sys
import django
from django.db import connections
from django.db.utils import OperationalError

# Agrega la ruta al segundo nivel 'app'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Configura la variable de entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

def test_database_connection():
    db_conn = connections['default']
    try:
        db_conn.ensure_connection()
        connected = True
    except OperationalError:
        connected = False
    assert connected, "❌ No se pudo conectar a la base de datos"
