import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_access.json', scope)
client = gspread.authorize(creds)

sheet_name = "BotData"
sheet = client.open(sheet_name).sheet1

#print(sheet.get_all_resords())
#row = ["test", "testo"]
#sheet.insert_row(row, 3)
