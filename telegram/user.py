from telegram import bot
from telegram.decorators import *
from db.manager import userManager


@bot.message_handler(commands=['auth'])
@private
@logging
def send_greeting(message):
    if message.chat.type == "private":
        userManager.add_user(id=message.from_user.id,
                             user_name=message.from_user.username,
                             first_name=message.from_user.first_name,
                             last_name=message.from_user.last_name)
    bot.reply_to(message, "Greetings! The bot recognised you.")
