import telebot
import os
from collections import defaultdict
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

from responses import *

#token = S3Connection(os.environ['TOKEN'])
bot_token = os.environ.get('TOKEN')
bot = telebot.TeleBot(bot_token)

# Data
sheet_link = "https://docs.google.com/spreadsheets/d/16hsfTo6p2ZRhPvwg3fSXJUSkAcx15HRz7unaOubSBOs/edit#gid=0"

google_token = json.loads(os.environ.get('GOOGLE_ACCESS'))

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(google_token, scope)
client = gspread.authorize(creds)

sheet_name = "BotData"
sheet = client.open(sheet_name).sheet1

# Responses




# Handlers
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, help_response)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, start_response)

@bot.message_handler(commands=['sheet_link'])
def send_help(message):
    bot.send_message(message.from_user.id, sheet_link)

@bot.message_handler(commands=['sheet_display'])
def send_help(message):
    bot.send_message(message.from_user.id, "PLACEHOLDER")

@bot.message_handler(content_types=['text'])
def send_greetings(message):
    bot.send_message(message.from_user.id, responses[message.text.lower()])



#/sheet_link
#/sheet_display


bot.polling()
