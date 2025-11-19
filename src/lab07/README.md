python -m pytest tests/test_text.py
строка для запуска в CLI из корня папки

```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n

##Параметризуем 
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected  


@pytest.mark.parametrize(
    "source, expected", 
    [
        ("привет мир", ["привет", "мир"]),
        ("мама,папа,сестра!", ["мама", "папа", "сестра"]),
        ("email@example.com сайт.ру", ["email", "example", "com", "сайт", "ру"]),
        ("!!!", []),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["я", "люблю", "python", "я", "люблю", "код"], {"я": 2, "люблю": 2, "python": 1, "код": 1}), 
        (["один", "два", "три"], {"один": 1, "два": 1, "три": 1}),
        (["lala", "la", "lala", "lalala", "lala"], {"lala": 3, "la": 1, "lalala": 1}), 
    ],
)
def test_count_freq_and_top_n(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, n, expected",
    [
        ({"я": 2, "люблю": 2, "python": 1, "код": 1}, 2, [("люблю", 2), ("я", 2)]),
        ({"один": 1, "два": 1, "три": 1}, 2, [("два", 1), ("один", 1)]),
        ({"lala": 3, "la": 1, "lalala": 1}, 2, [("lala", 3), ("la", 1)]),
    ],
)
def test_top_n_tie_breaker(source, n, expected):
    assert top_n(source, n) == expected
```


python -m pytest tests/test_json_csv.py

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