import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        # 1. Читаем JSON
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        # 2. Проверяем что это список словарей
        if not data or not isinstance(data, list):
            raise ValueError
        
        # 3. Получаем все возможные заголовки
        all_keys = set()
        for item in data:
            if not isinstance(item, dict):
                raise ValueError
            all_keys.update(item.keys())
        
        # 4. Записываем CSV
        with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=all_keys) #записывает список словарей
            writer.writeheader()
            for row in data:
                # Заполняем отсутствующие поля пустыми строками
                complete_row = {key: row.get(key, "") for key in all_keys}
                writer.writerow(complete_row)
                
    except FileNotFoundError:
        raise FileNotFoundError

def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        # 1. Читаем CSV
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        
        # 2. Проверяем что есть данные
        if not data:
            raise ValueError
        
        # 3. Записываем JSON
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
            
    except FileNotFoundError:
        raise FileNotFoundError
    