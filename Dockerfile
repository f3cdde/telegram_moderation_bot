# Use uma imagem base oficial do Python
FROM python:3.8-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt ./

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . .

# Defina a variável de ambiente PYTHONPATH para incluir o diretório /app
ENV PYTHONPATH=/app

# Exponha a porta 5000
EXPOSE 5000

# Comando para iniciar o bot
CMD ["python", "app/bot.py"]
