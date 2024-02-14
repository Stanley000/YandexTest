import csv
import json
import requests

# Параметры запроса
url = 'http://siem.yandex.ru/input'
#local_url = 'http://localhost:8686/input'
headers = {'Content-Type': 'application/json'}

# Чтение CSV файла и отправка данных в SIEM
with open('super_mega_critical.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Преобразование строки CSV в JSON
        json_data = json.dumps(row)
        
        # Отправка данных в SIEM
        response = requests.post(url, data=json_data, headers=headers)
        
        # Проверка
        if response.status_code == 200:
            print("Данные успешно отправлены в SIEM")
        else:
            print(f"Ошибка отправки данных в SIEM. Код ошибки: {response.status_code}")
