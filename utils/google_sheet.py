def get_header(google_sheet):
    return "**" + " ".join(list(google_sheet[0].keys())) + "**"

def get_row(google_sheet, n):
    if n > len(google_sheet):
        return f"The table is only {len(google_sheet)} long! Try again"
    else:
        return " ".join([str(value) for value in google_sheet[int(n-1)].values()])
