# test_import.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_full_rest.settings')
django.setup()

try:
    from tests.userss.test_userss import test_userss_creation
    print(f"Importacion exitosa")
except ImportError as e:
    print(f"Error de importación: {e}")
