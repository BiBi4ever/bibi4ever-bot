import telebot
import os
from collections import defaultdict

#token = S3Connection(os.environ['TOKEN'])
token = os.environ.get('TOKEN')
print(token)
bot = telebot.TeleBot(token)

responses = {
"hi": "Hello you!",
"hello": "Hello you!"
}

default_response = "I don't understand you :( Please type in the \help command to see what I can do"

responses = defaultdict(lambda: default_response, responses)




#responses.setdefault(key, default=DEFAULT)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "A human?!")

@bot.message_handler(content_types=['text'])
def send_greetings(message):
    bot.send_message(message.from_user.id, responses[message.text.lower()])


bot.polling()
