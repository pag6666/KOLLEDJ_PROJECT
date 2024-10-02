import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

USER_GMAIL = "userjson93@gmail.com"
dir_parser_box = os.getcwd() + "\\" +"ParserBox"
SERVICE_ACCOUNT_FILE = dir_parser_box+"\\gs_credentials.json"

if(os.path.exists(dir_parser_box) == False):
    os.mkdir(dir_parser_box)
    exit(1)

print(os.getcwd() + SERVICE_ACCOUNT_FILE)
print("Get: " + SERVICE_ACCOUNT_FILE)
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)

client = gspread.auth.authorize(credentials)

sheet = client.create("GoogleSheet")

sheet.share(USER_GMAIL, perm_type='user', role='writer')
