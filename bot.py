import telebot
import os
from collections import defaultdict
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#token = S3Connection(os.environ['TOKEN'])
token = os.environ.get('TOKEN')
print(token)
bot = telebot.TeleBot(token)

# Data
sheet_link = "https://docs.google.com/spreadsheets/d/16hsfTo6p2ZRhPvwg3fSXJUSkAcx15HRz7unaOubSBOs/edit#gid=0"
"""
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_access.json', scope)
client = gspread.authorize(creds)

sheet_name = "BotData"
sheet = client.open(sheet_name).sheet1
"""

# Responses

responses = {
"hi": "Hello you!",
"hello": "Hello you!"
}

default_response = "I don't understand you :( Please type in the /help command to see what I can do"
start_response = "A human?! I am so happy! Please type in the /help command to see what I can do"
help_response = "Here's a list of available commands: \n:panda: /help - displays this message\n:koala: /start - displays start message\n:see_no_evil: /sheet_link - shows link to sheet\n:see_no_evil: /sheet_display - shows all rows in sheet"


responses = defaultdict(lambda: default_response, responses)


# Handlers

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, start_response)

@bot.message_handler(content_types=['text'])
def send_greetings(message):
    bot.send_message(message.from_user.id, responses[message.text.lower()])

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, help_response)

@bot.message_handler(commands=['sheet_link'])
def send_help(message):
    bot.send_message(message.from_user.id, sheet_link)

@bot.message_handler(commands=['sheet_display'])
def send_help(message):
    bot.send_message(message.from_user.id, "PLACEHOLDER")

#/sheet_link
#/sheet_display


bot.polling()
