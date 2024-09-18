import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
USER_GMAIL = "userjson93@gmail.com"
SERVICE_ACCOUNT_FILE = "gs_credentials.json"

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)

client = gspread.auth.authorize(credentials)

#sheet = client.create("FirstSheet")

#sheet.share(USER_GMAIL, perm_type = "user", role = "writer")



NameSheet = "FirstSheet"

def ClientOpen(nameSheet):

  return client.open(nameSheet).sheet1

#db = pd.read_csv("C:\\Users\\pargev\\Desktop\\task1\\source\\prices.csv")

#sheet.update([db.columns.values.tolist()] + db.values.tolist())
def CreateSheet(nameSheet):
    return client.create(nameSheet)

def SetNewData(filePath:str, nameSheet:str):
    db = pd.read_csv(filePath)

    ClientOpen(nameSheet).update([db.columns.values.tolist()] + db.values.tolist())

def PrintAllFiles():
    file_list = client.list_spreadsheet_files()
    for file in file_list:
        print(f"\nname: {file['name']}, ID: {file['id']}")
    
       
        sheet = client.open_by_key(file['id'])
    
       
        for worksheet in sheet.worksheets():
            print(f"Лист: {worksheet.title}")
        
           
            data = worksheet.get_all_values()
        
            
            for row in data:
                print(row)

def PrintSheet(nameSheet):
    id:str = ""

    if CheckFileSheet(nameSheet):
       
       id = GetIdFromNameSheet(nameSheet)
       sheet = client.open_by_key(id)
       
       for work in sheet.worksheets():
           
           data = work.get_all_values()
           for row in data:
               print(row)
        

def GetDataFromNameSheet(nameSheet):
    id:str = ""

    if CheckFileSheet(nameSheet):
       
       id = GetIdFromNameSheet(nameSheet)
       sheet = client.open_by_key(id)
       
    return sheet.get_worksheet()
        


def CheckFileSheet(nameSheet:str):
    r = False 
    file_list = client.list_spreadsheet_files()  
   
    for file in file_list:
       
        if file['name'] == nameSheet:     
           
            r = True
            break

    return r

def GetIdFromNameSheet(nameSheet):
    file_list = client.list_spreadsheet_files()
    id = ""
    for file in file_list:
        if file['name'] == nameSheet:
            id = file['id']
            break
        
    return id

