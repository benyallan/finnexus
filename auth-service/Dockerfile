# Dockerfile

FROM python:3.12

# Set working directory
WORKDIR /app

# Copia os arquivos de requisitos
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instala o ulid-py
RUN pip install ulid-py

RUN pip install python-dotenv

# Comando para rodar o app
CMD ["python", "src/main.py"]
