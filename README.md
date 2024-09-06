# Telegram Moderation Bot

Este é um bot de moderação automática para Telegram, desenvolvido em Python e Docker. O bot monitora mensagens em um grupo e toma ações como excluir mensagens inadequadas ou banir usuários que violarem as regras.

## Estrutura do Projeto

telegram_moderation_bot/
│
├── app/
│   ├── __init__.py
│   ├── bot.py
│   ├── config.py
│   ├── handlers.py
│   ├── utils.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md


## Dependências

- python-telegram-bot
- python-dotenv

## Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/telegram_moderation_bot.git

2. Navegue até o diretório do projeto:
   cd telegram_moderation_bot

3. Crie um arquivo .env com as seguintes variáveis de ambiente:
   TELEGRAM_TOKEN=seu_telegram_token
   MODERATION_KEYWORDS=palavra1,palavra2,palavra3
   ADMIN_USER_ID=seu_id_de_usuario

4. Construa e inicie os serviços Docker:
   docker-compose up --build

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.


### Passos para Garantir que o Projeto está Funcional

1. **Clone o repositório**: Certifique-se de que você pode clonar o repositório do GitHub.

2. **Navegue até o diretório do projeto**: Certifique-se de que você está no diretório onde o arquivo `bot.py` está localizado.

3. **Crie os arquivos necessários**: Certifique-se de que todos os arquivos mencionados acima estão presentes e configurados corretamente.

4. **Construa e inicie os serviços Docker**: Construa e inicie os serviços Docker com o comando:

   docker-compose up --build