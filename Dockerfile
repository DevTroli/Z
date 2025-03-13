# Dockerfile
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

