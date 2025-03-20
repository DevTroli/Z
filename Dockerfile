# Estágio de construção
FROM python:3.10-slim as builder

WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências em um diretório temporário
RUN pip install --user --no-cache-dir -r requirements.txt

# Estágio de produção
FROM python:3.10-slim as production

WORKDIR /app

# Copia apenas as dependências instaladas
COPY --from=builder /root/.local /root/.local
COPY . .

# Adiciona o diretório de dependências ao PATH
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar o servidor com Gunicorn
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
