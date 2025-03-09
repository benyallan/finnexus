# Usa a imagem oficial do Python 3.12 como base
FROM python:3.12

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia apenas o arquivo de dependências primeiro para aproveitar cache de build
COPY requirements.txt .

# Instala todas as dependências de uma vez para otimizar camadas
RUN pip install --no-cache-dir -r requirements.txt ulid-py python-dotenv

# Copia apenas a pasta src para dentro do contêiner
COPY src/ src/

# Define o comando padrão ao rodar o contêiner
ENTRYPOINT ["python", "src/main.py"]
