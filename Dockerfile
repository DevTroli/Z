FROM python:3.10-slim

# Evita que Python crie arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Garante que a saída do Python seja enviada imediatamente para o terminal
ENV PYTHONUNBUFFERED=1

# Cria e define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
  postgresql-client \
  && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requisitos primeiro para aproveitar o cache do Docker
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copia o resto do código para o container
COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta que o Gunicorn vai usar
EXPOSE 8000

# Comando para iniciar o Gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
