import telebot
#from boto.s3.connection import S3Connection
import os

#token = S3Connection(os.environ['TOKEN'])
token = os.environ.get('TOKEN')
print(token)
bot = telebot.TeleBot(token)

responses = {
"hi": "Hello you!",
"hello": "Hello you!"
}

#responses.setdefault(key, default=DEFAULT)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "A human?!")

@bot.message_handler(content_types=['text'])
def send_greetings(message):
    if message.text.lower() in responses:
        bot.send_message(message.from_user.id, responses[message.text.lower()])
    else:
        bot.send_message(message.from_user.id, "Type \'Hello\' to begin")


bot.polling()
