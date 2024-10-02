import source.http_parser
import source.my_lib
import pandas as pd
import os
#source.market_parse.get_price_from_yandex_market("")

patern_site = ["https://market.yandex.ru", "https://globus-online.kg","https://lenta.com"]

inputSheet = "InputSheetStr"
outputSheet = "OutputSheetStr"

links_list = []
name_list = []
found_price = []

def remove_unwanted_chars(text, unwanted_chars):
    # Создание таблицы соответствия символов для удаления
    translation_table = str.maketrans('', '', unwanted_chars)
    # Применение перевода к строке
    cleaned_text = text.translate(translation_table)
    return cleaned_text

def Init():
    print("Start")
    if source.my_lib.CheckFileSheet(inputSheet) == False:
        source.my_lib.CreateSheet(inputSheet)
        print(f"Create sheet: {inputSheet};")

    if source.my_lib.CheckFileSheet(outputSheet) == False:
        source.my_lib.CreateSheet(outputSheet)
        print(f"Create sheet: {outputSheet};")


def Working():
    

    if source.my_lib.CheckFileSheet(inputSheet):
        get_id_inpout = source.my_lib.GetIdFromNameSheet(inputSheet)
        client = source.my_lib.GetClient()
        sheet = client.open_by_key(get_id_inpout)
        for work in sheet.worksheets():
            data = work.get_all_values()
            i = 0
            for row in data:
                if(i != 0 ):
                    print(f"Get Links {row[1]}")
                    print(f"Get Name {row[0]}")
                    tx1:str = row[0]
                    tx2:str = row[1]
                    tx1 = remove_unwanted_chars(tx1,',')
                    tx2 = remove_unwanted_chars(tx2,',')
                    name_list.append(tx1)
                    links_list.append(tx2)
                i = i + 1
        # this is point var !!!
        print("Success Get")
        for i in links_list:
            link:str = i
            if  link.startswith(patern_site[0]):
                print("OPEN YANDEX MARKET")
                found_price.append(source.http_parser.get_price_from_yandex_market(i))
            elif link.startswith(patern_site[1]):
                print("GLOBUS")
                found_price.append(source.http_parser.get_price_from_globus(i))
            elif link.startswith(patern_site[2]):
                print("LENTA")
                found_price.append(source.http_parser.get_price_from_lenta(i))
            
        
        
        temp_list = [[]]
        index = 0
        temp_list.append(["Name", "Price"])
        for i in found_price:
            temp_list.append([name_list[index], i])
            index = index + 1
        dir_parser_box = os.getcwd() + "\\" +"ParserBox"
        
        source.http_parser.save_to_csv(temp_list, dir_parser_box + "\\save.csv")
        if source.my_lib.CheckFileSheet(outputSheet) :
            db = pd.read_csv(dir_parser_box + "\\save.csv")
            get_id_output = source.my_lib.GetIdFromNameSheet(outputSheet)
            client = source.my_lib.GetClient()
            sheet = client.open_by_key(get_id_output)
            db.fillna('', inplace=True)
            sheet.sheet1.update([db.columns.values.tolist()] + db.values.tolist())

       


        

def Close():
    
    print("Close")


def Main():

    Init()
    
    Working()
    
    Close()

if __name__ == "__main__":
    Main()