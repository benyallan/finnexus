# Usa a imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do auth-service para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "src/main.py"]
