snowflake = u'\U00002744'

responses = {
"hi": "Hello you!",
"hello": "Hello you!"
}

default_response = "I don't understand you :( Please type in the /help command to see what I can do"
start_response = "A human?! I am so happy! Please type in the /help command to see what I can do"
help_response = f"""Here's a list of available commands: \n
                {snowflake} /help - displays this message\n
                {snowflake} /start - displays start message\n
                {snowflake} /sheet_link - shows link to sheet\n
                {snowflake} /sheet_display - shows all rows in sheet"""


responses = defaultdict(lambda: default_response, responses)
