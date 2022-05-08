import os
from pathlib import Path

SECRET_KEY = 'django-insecure-h!#n)0$=z&@0d_-8*+-w&*&d4j*3108oy9shgy!2c3a#(ck3ad'

DEBUG = True

EMAIL_HOST_PASSWORD = 'ypjcgdxgidywdygi'

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}