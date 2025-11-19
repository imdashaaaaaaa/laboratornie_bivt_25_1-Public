python -m pytest tests/test_json_csv.py
строка для запуска в CLI из корня папки

```python
import pytest
import json, csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json

##Позитивный сценарий: конвертация JSON → CSV, совпадает количество записей, совпадает набор ключей/заголовков (например, name, age)
def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    json_data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())

##Негативный сценарий: пустой входной файл → ожидаем ValueError
def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "out.csv"
    empty_json_data = []
    src.write_text(json.dumps(empty_json_data), encoding="utf-8")

    with pytest.raises(ValueError):  
        json_to_csv(str(src), str(dst))


##Негативный сценари: JSON не список (некорректно записан) → ожидаем ValueError
def test_json_to_csv_invalid_json(self, tmp_path: Path):
    src = tmp_path / "invalid.json"
    dst = tmp_path / "out.csv"
    invalid_json_data = '{"name": "Alice", "age": 22'
    src.write_text(json.dumps(invalid_json_data),  encoding="utf-8")
        
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


##Позитивный сценарий: конвертация CSV → JSON, совпадает количество записей, совпадает набор ключей/заголовков (например, name, age)
def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    csv_data = """name,age
Alice,22
Bob,25"""

    src.write_text(csv_data, encoding="utf-8" )
    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        result_data  = json.load(f)

    assert isinstance(result_data, list) and len(result_data) == 2
    assert set(result_data[0]) == {"name", "age"}


##Негативный сценарий: несуществующий путь к файлу → ожидаем FileNotFoundError
def test_file_not_exist(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json") #пытаемся прочитать несуществующий файл


##with pytest.raises(ОжидаемоеИсключение):
   ## код_который_должен_выбросить_исключение
```
<img width="1405" height="289" alt="Снимок экрана 2025-11-19 121830" src="https://github.com/user-attachments/assets/49678170-d09e-42a1-be0d-2742d1302d71" />
