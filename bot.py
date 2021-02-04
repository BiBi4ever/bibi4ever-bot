import telebot
#from boto.s3.connection import S3Connection
import os

#token = S3Connection(os.environ['TOKEN'])
token = os.environ.get('TOKEN')
print(token)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "A human?!")
    
@bot.message_handler(content_types=['text'])
def send_greetings(message):
    if "hello" in message.text.lower() or "hi" in message.text.lower():
        bot.send_message(message.from_user.id, "Hello you!")
    else:
        bot.send_message(message.from_user.id, "Type \'Hello\' to begin")


bot.polling()
