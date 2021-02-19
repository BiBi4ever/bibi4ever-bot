def launch_google_client(google_token):
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_dict(google_token, scope)
    client = gspread.authorize(creds)
return gspread.authorize(creds)
