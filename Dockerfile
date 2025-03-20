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

# Copia o script de inicialização
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Comando para iniciar o script
CMD ["/app/start.sh"]
