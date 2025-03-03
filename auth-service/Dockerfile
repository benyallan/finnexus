# Dockerfile

FROM python:3.12

# Set working directory
WORKDIR /app

# Copia os arquivos de requisitos
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instala o ulid-py
RUN pip install ulid-py

# Copia o código para o container
COPY . .

# Comando para rodar o app
CMD ["python", "src/main.py"]
