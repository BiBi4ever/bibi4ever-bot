# libraries
import telebot
import os
from collections import defaultdict
import json

# user modules
from utils.auth import launch_google_client
from utils.google_sheet import get_row, get_header
from data.responses import *

#tokens and clients
bot_token, google_token = os.environ.get('TOKEN'), json.loads(os.environ.get('GOOGLE_ACCESS'))
bot, google_client = telebot.TeleBot(bot_token), launch_google_client(google_token)

# Data
sheet_link, sheet_name = os.environ.get('SHEET_LINK'), os.environ.get('SHEET_NAME')
google_sheet = google_client.open(sheet_name).sheet1.get_all_records()

# Responses
# auto help message
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.from_user.id, help_response)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, start_response)

@bot.message_handler(commands=['sheet_link'])
def sheet_link(message):
    bot.send_message(message.from_user.id, sheet_link)

@bot.message_handler(commands=['sheet_display'])
def sheet_display(message):
    header = get_header(google_sheet)
    row1 = get_row(google_sheet, 1)
    row2 = get_row(google_sheet, 2)
    row_count = "Total records #" + str(len(google_sheet))

    response = "\n".join([header, row1, row2, "...", row_count])
    bot.send_message(message.from_user.id, response, parse_mode="markdown")

@bot.message_handler(commands=['sheet_row'])
def sheet_row(message):
    # user prompt "Type in row number"
    prompt = bot.send_message(message.from_user.id, "type in row number")
    bot.register_next_step_handler(prompt, send_row)

def send_row(message):
    try:
        n = int(message.text)
        rown = get_row(google_sheet, n)
        bot.send_message(message.from_user.id, rown)
    except:
        warning = bot.send_message(message.from_user.id, "Not a number, try again!")
        bot.register_next_step_handler(warning, sheet_row)

"""
@bot.message_handler(content_types=['text'])
def send_greetings(message):
    bot.send_message(message.from_user.id, responses[message.text.lower()])
"""

bot.polling()
