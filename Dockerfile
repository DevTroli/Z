# Estágio de construção
FROM python:3.10-slim as builder

WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências globalmente (sem --user)
RUN pip install --no-cache-dir -r requirements.txt

# Estágio de produção
FROM python:3.10-slim as production

WORKDIR /app

# Copia as dependências instaladas
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código da aplicação
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar o servidor com Gunicorn
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
