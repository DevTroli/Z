#!/bin/bash

# Define PORT como 8000 se não estiver definido
export PORT=${PORT:-8000}

# Executa as migrações
python manage.py migrate

# Inicia o servidor Gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
