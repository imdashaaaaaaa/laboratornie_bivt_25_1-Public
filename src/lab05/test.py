import sys
import os
from pathlib import Path

# Добавляем текущую директорию в путь (в начало)
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Импортируем напрямую из текущей папки
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx

    
PROJECT_ROOT = Path(__file__).parent.parent.parent
    
json_source = PROJECT_ROOT / "data" / "samples" / "people.json"
csv_source = PROJECT_ROOT / "data" / "samples" / "people.csv"
        
output_csv = PROJECT_ROOT / "data" / "out" / "people_from_json.csv"
output_json = PROJECT_ROOT / "data" / "out" / "people_from_csv.json"
output_xlsx = PROJECT_ROOT / "data" / "out" / "people.xlsx"

try:
    json_to_csv(str(json_source), str(output_csv))
            
    csv_to_json(str(csv_source), str(output_json))

    csv_to_xlsx(str(csv_source), str(output_xlsx))
            
except Exception as e:
    print(f"Ошибка: {e}")
