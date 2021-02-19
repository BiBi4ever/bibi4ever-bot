import telebot
import os
from collections import defaultdict
import json
from auth import launch_google_client

from responses import *

#tokens = S3Connection(os.environ['TOKEN'])
bot_token = os.environ.get('TOKEN')
google_token = json.loads(os.environ.get('GOOGLE_ACCESS'))

#clients
bot = telebot.TeleBot(bot_token)
google_client = launch_google_client(google_token)


# Data
sheet_link = "https://docs.google.com/spreadsheets/d/16hsfTo6p2ZRhPvwg3fSXJUSkAcx15HRz7unaOubSBOs/edit#gid=0"
sheet_name = "BotData"
google_sheet = google_client.open(sheet_name).sheet1

# Responses
# Handlers
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
    result = google_sheet.get_all_records()

    header = "**" + " ".join(list(result[0].keys())) + "**"
    row1 = " ".join([str(x) for x in result[0].values()])
    row2 = " ".join([str(x) for x in result[1].values()])
    row_count = "Total records #" + str(len(result))

    response = "\n".join([header, row1, row2, "...", row_count])
    bot.send_message(message.from_user.id, response, parse_mode="markdown")

@bot.message_handler(commands=['sheet_row'])
def sheet_row(message):
    # user prompt "Type in row number"
    prompt = bot.send_message(message.from_user.id, "type in row number")
    bot.register_next_step_handler(prompt, send_row)

def send_row(message):
    n = int(message.text)
    result = google_sheet.get_all_records()
    rown = " ".join([str(x) for x in result[int(n-1)].values()])
    bot.send_message(message.from_user.id, rown)


@bot.message_handler(content_types=['text'])
def send_greetings(message):
    bot.send_message(message.from_user.id, responses[message.text.lower()])


bot.polling()
