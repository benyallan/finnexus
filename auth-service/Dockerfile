# Usa a imagem oficial do Python 3.12 (não-slim)
FROM python:3.12

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema necessárias para o mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    libmariadb-dev \
    libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Restante do Dockerfile (cópia do código, etc.)
COPY src/ ./src
ENV FLASK_ENV=development
ENV FLASK_APP=src/main.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
