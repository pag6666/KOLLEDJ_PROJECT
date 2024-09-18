import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_price_from_yandex_market(url):
    # Отправляем GET-запрос на страницу
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Ошибка запроса: {response.status_code}")
        return None
    
    # Парсим страницу
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Извлекаем цену
    price_tag = soup.find('span', class_='_2r9lI')  # Замените на актуальный класс для цены
    if price_tag:
        price = price_tag.text.strip()
        return price
    else:
        print("Цена не найдена")
        return None

def save_to_csv(data, filename):
    # Сохраняем данные в CSV файл
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


#'C:\\Users\\Pargev\\Desktop\\task1\\init\\prices.csv'

def save_price_in_file(url_item:str, file_path:str):
    # URL продукта на Яндекс.Маркете
    product_url = url_item  # Замените на фактический URL продукта
    
    # Получаем цену
    price = get_price_from_yandex_market(product_url)
    
    if price.__len__() > 0:
        # Создаем список данных
        data = [{'Product URL': product_url, 'Price': price}]
        
        # Сохраняем данные в CSV
        save_to_csv(data, file_path)
        print("Данные успешно сохранены в prices.csv")


#пример
#get_price_ya('https://market.yandex.ru/product--smart-zont-mini-zont-avtomat-3-slozheniia-kupol-98-sm-8-spits-obratnoe-slozhenie-sistema-antiveter/600536637?sku=102245799556&uniqueId=1254254&do-waremd5=zzaXYYE8aHrcGfV3TAnnVA')
