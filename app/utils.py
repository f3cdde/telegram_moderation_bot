from telegram import Update
from telegram.ext import CallbackContext
from app.config import Config

def is_message_inappropriate(message: str) -> bool:
    for keyword in Config.MODERATION_KEYWORDS:
        if keyword.lower() in message.lower():
            return True
    return False

def take_action(update: Update, context: CallbackContext, user_id: int):
    if user_id != Config.ADMIN_USER_ID:
        update.message.delete()
        context.bot.kick_chat_member(update.message.chat_id, user_id)
        context.bot.send_message(chat_id=update.message.chat_id, text=f'Usuário {user_id} foi banido por violar as regras.')
