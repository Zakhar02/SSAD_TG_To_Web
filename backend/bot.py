import os

# import telebot
from .models import Channel, Message

# TOKEN = os.environ.get('TELEGRAM_TOKEN')
# bot = telebot.TeleBot(TOKEN)

# @bot.channel_post_handler(content_types=['text']) #for now it handles text messages only
# def post_text_message(message):
#     channels = Channel.objects.filter(chat_name=message.chat.title)
#     print(list(Channel.objects.all()))
#     if channels.count() == 0: #if not exists in Channels list
#         Channel(chat_name=message.chat.title).save() #aading another channel

#     Message(chat_name=channels.first(), chat_id=message.chat.id,
#             content_type=message.content_type, message_id=message.message_id, text = message.text).save() #saving a message to DB

# def run(): #used in manage.py command
#     bot.polling()