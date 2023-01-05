"""This module contains functions for working with strings."""

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Use the service account credentials to authenticate with Google
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/<spreadsheet_id>/edit')

# Select the first sheet
worksheet = sh.sheet1

# Access the data in the sheet
input_string = worksheet.acell('A1').value

# Use the input string in your script
parts = input_string.split(' ')
part_1 = parts[0]
part_2 = parts[1]
part_3 = parts[3]
part_4 = parts[4]
part_5 = ' '.join(parts[5:])
output_string = f"{part_1}@{part_2} {part_3} {part_5} SEE {part_4}"
print(output_string)


import sys
print(sys.path)
