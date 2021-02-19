def get_header(google_sheet):
    return "**" + " ".join(list(google_sheet[0].keys())) + "**"

def get_row(n):
    return " ".join([str(value) for value in google_sheet[int(n-1)].values()])
