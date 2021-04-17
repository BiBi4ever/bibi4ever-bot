import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_access.json', scope)
client = gspread.authorize(creds)

sheet_name = "BotData"
sheet = client.open(sheet_name).sheet1

#row = ["test", "testo"]
#sheet.insert_row(row, 3)

result = sheet.get_all_records()

primer1location = result[0]['shelf_number']

header = " ".join(list(result[0].keys()))
row1 = " ".join([str(x) for x in result[0].values()])
row2 = " ".join([str(x) for x in result[1].values()])
row_count = "Total records #" + str(len(result))

response = "\n".join([header, row1, row2, "...", row_count])




print(response)
