from telegram import Update
from telegram.ext import CallbackContext
from app.config import Config
from app.utils import is_message_inappropriate, take_action

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Olá! Eu sou o bot de moderação. Estou aqui para manter o grupo seguro.')

def handle_message(update: Update, context: CallbackContext):
    message = update.message.text
    user_id = update.message.from_user.id

    if is_message_inappropriate(message):
        take_action(update, context, user_id)
