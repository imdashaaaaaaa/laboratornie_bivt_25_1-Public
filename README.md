## Лабораторная №1

### Задание 1
```python
name=input("Имя: ") 
age=int(input("Возраст: ")) 
print("Привет, ", name, "! Через год тебе будет ", age+1, ".", sep="")
```
![ex01](https://github.com/user-attachments/assets/ecebae4d-c888-4c35-8e54-02ee1a0388e5)

### Задание 2
```python
a=(input("a: "))
a_finish=a.replace(",",".")
b=(input("b: "))
b_finish=b.replace(",",".")
summa=float(a_finish)+float(b_finish)
summa=round(summa, 2)
avg=summa/2
avg=round(avg, 2)
print("sum=", summa, "; avg=", avg, sep="")
```
![ex02](https://github.com/user-attachments/assets/e03fb6f6-355e-4fd4-83ee-e581e580dec7)

### Задание 3
```python
price=float(input("Цена(₽): "))
discount=float(input("Скидка(%): "))
vat=float(input("НДС(%): "))
base=round(price*(1-discount/100), 2)
vat_amount=round(base*(vat/100), 2)
total=round(base+vat_amount, 2)
print("База после скидки: ", base, " ₽", sep="")
print("НДС: ", vat_amount, " ₽", sep="")
print("Итого к оплате: ", total, " ₽", sep="")
```
![ex03](https://github.com/user-attachments/assets/51ea0f82-64bf-4c4f-87f2-ec1157fb4927)

### Задание 4
```python
m=int(input("Минуты: "))
hours=m//60
minutes=m%60
print(hours,":", f"{minutes:02d}", sep="")
```
![ex04](https://github.com/user-attachments/assets/ba6553c5-6833-42b5-bdad-9f450d860cb7)

### Задание 5
```python
full_name=input("ФИО: ")
strip_name=full_name.strip()
parts_name=strip_name.split()
initials=""
len_full_name=0
for i in range (3):
    len_full_name+=len(parts_name[i])
    initials+=parts_name[i][0].upper()
print("Инициалы:", initials)
print("Длина (символов):", len_full_name+2)
```
![ex05](https://github.com/user-attachments/assets/6e9bacbb-c4a1-4ba2-bdd9-e3f6565d81d2)



## Лабораторная №2
### Задание 1 (arrays)
```python
def min_max(nums:list[float | int]) -> tuple [float | int, float | int]:
    if not nums: 
        return ValueError 
    return tuple((min(nums), max(nums)))

def unique_sorted(nums: list[float|int]) -> list[float|int]:
    return tuple(sorted(set(nums)))

def flatten(mat: list[list | tuple]) -> list:
    array=[]
    for element in mat:
         if not isinstance(element, (list, tuple)):
             return TypeError
         array.extend(element)
    return array

print(min_max([3, -1, 5, 5, 0]), min_max([42]), min_max([-5,-2,-9]), min_max([]), min_max([1.5,2,2.0,-3.1])) #Тест-кейсы min_max

print(unique_sorted([3,1,2,1,3]), unique_sorted([]), unique_sorted([-1,-1,0,2,2]), unique_sorted([1.0, 1, 2.5, 2.5, 0])) #Тест-кейсы unique_sorted

print(flatten([[1,2],[3,4]]), flatten([[1,2],(3,4,5)]), flatten([[1],[],[2,3]]), flatten([[1,2],"ab"])) #Тест-кейс flatten
```
<img width="1511" height="781" alt="arrays_ph" src="https://github.com/user-attachments/assets/7fa267aa-95b7-40ca-abd8-d10b441e7b18" />


### Задание 2 (matrix)
```python
def is_valid_matr(mat: list[list[float | int]]) -> bool:
    for i in range (len(mat)):
        if len(mat[i])!=0 and len(mat[0])!=len(mat[i]):
            return False
    return True 

def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
        return []
    if is_valid_matr(mat)==False:
        return ValueError

    result = []
    for columns in range (len(mat[0])):
        new_row=[]
        for row in range (len(mat)):
            new_row.append(mat[row][columns])
        result.append(new_row)

    return result 

print(transpose([[1, 2, 3]]), transpose([[1], [2], [3]]), transpose([[1, 2], [3,4]]), transpose([]), transpose([[1, 2], [3]])) #Тест-кейс transpose

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if is_valid_matr(mat)==False:
        return ValueError
    
    result=[]
    for row in mat:
        result.append(sum(row))

    return result

print(row_sums([[1,2,3], [4,5,6]]), row_sums([[-1,1], [10,-10]]), row_sums([[0,0], [0,0]]), row_sums([[1,2], [3]])) #Тест-кейс row_sums

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if is_valid_matr(mat)==False:
        return ValueError
    
    new_mat=(transpose(mat))
    result=(row_sums(new_mat))

    return result

print(col_sums([[1,2,3], [4,5,6]]), col_sums([[-1,1], [10,-10]]), col_sums([[0,0], [0,0]]), col_sums([[1,2], [3]])) #Тест-кейс col_sums
```
<img width="1507" height="652" alt="image" src="https://github.com/user-attachments/assets/2644952f-b11a-4b7c-bf9f-9bd36039964f" />


### Задание 3 (tuples)
```python
def format_record(rec: tuple[str, str, float]) -> str:
    cleaned_fio=rec[0].strip().split()
    surname=cleaned_fio[0][0].upper()
    if len(cleaned_fio)==3:
        form_fio=f"{surname}{cleaned_fio[0][1:]} {cleaned_fio[1][0].upper()}.{cleaned_fio[2][0].upper()}."
    elif len(cleaned_fio)==2:
        form_fio=f"{surname}{cleaned_fio[0][1:]} {cleaned_fio[1][0].upper()}."
    else:
        return ValueError
    
    group=rec[1].strip()
    if not group:
        return ValueError
    
    gpa=f"{float(rec[2]):.2f}"

    return f"{form_fio}, гр. {group}, GPA {gpa}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record((" К ", "", 4.877)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.5689)))
```
<img width="1189" height="837" alt="tuples_ph" src="https://github.com/user-attachments/assets/fefdf5d8-7d41-4e3a-b6ef-de20798b0564" />

## Лабораторная №3
### Задание A (text.py)
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    
    result = text
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'Е')
    
    if casefold:
        result = result.casefold()

    for char in ['\t', '\r', '\n']:
        result = result.replace(char, ' ')
    
    result = ' '.join(result.split())
    
    return result

import re

def tokenize(result: str) -> list[str]:

    pattern =  r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, result)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:

    count_words={}
    for word in tokens:
        count_words[word]=count_words.get(word, 0)+1 
    
    return count_words


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_items = sorted(freq.items(), key=lambda x: (x[0])) #по алфавиту
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1])) #по количеству в обратном порядке

    return sorted_items[:n]

if __name__ == "__main__":
    print (normalize ("ПрИвЕт\nМИр\t"))
    print (tokenize ("emoji 😀 не слово"))
    print (top_n(count_freq(["a","b","a","c","b","a"]), n=2))
```
<img width="1030" height="771" alt="A" src="https://github.com/user-attachments/assets/53cda335-dcc1-418e-bdc1-da5fd15e7b3f" />


### Задание B (text_stats.py)
```python
import sys
sys.path.append("C:/Users/Redmi/Desktop/ivt/laboratornie_bivt_25_1-Public/src")

from lib.text import normalize, tokenize, count_freq, top_n

text = sys.stdin.readline()

normalized_text = normalize(text)

tokens = tokenize(normalized_text)

count_words = count_freq(tokens)

top_words = top_n(count_words, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(count_words)}")
print("Топ-5:")

for word, count in top_words:
    print(f"{word}:{count}")
```
<img width="887" height="812" alt="B" src="https://github.com/user-attachments/assets/ff47b729-d04e-4873-a977-62aefe43e0a6" />

## Лабораторная №4
### Задание A (io_txt_csv.py)
```python
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError
    
    return p.read_text(encoding=encoding)

import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)

        if header is not None:
            w.writerow(header)
        if rows:
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError
        
        for r in rows:
            w.writerow(r)
```

### Задание B (text_stats.py)
```python
import sys
from pathlib import Path
sys.path.append("C:/Users/Redmi/Desktop/ivt/laboratornie_bivt_25_1-Public/src")
from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

input_path = PROJECT_ROOT / "data" / "input.txt"
output_path = PROJECT_ROOT / "data" / "report.csv"
p = read_text(input_path)
norm_p=normalize(p)
tokens=tokenize(norm_p)
count_word=count_freq(tokens)
top=top_n(count_word)

write_csv(top, output_path, ["word", "count"])

print("Всего слов:", len(tokens))
print("Уникальных слов:", len(count_word))
print("Топ-5:")
for x,y in top[:5]:
    print(f'{x}:{y}')
```
<img width="926" height="903" alt="test_A" src="https://github.com/user-attachments/assets/9a9b26ad-06ac-4155-820f-77e4c68dbbe4" />
<img width="907" height="848" alt="test_B" src="https://github.com/user-attachments/assets/336ec66b-b8ea-48f3-95e1-3b4d7ef20f7c" />

## Лабораторная №5
### Функции: 
### JSON -> CSV 
```python
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
```
### CSV -> JSON
```python
import json
import csv
from pathlib import Path

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
```
### CSV -> XLSX
```python
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        wb = Workbook() #создаем файл в экселе
        ws = wb.active #создаем активный лист в экселе
        ws.title = "Sheet1"
        
        # Читаем CSV и записываем в XLSX
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                ws.append(row)
        
        # Настраиваем авто-ширину колонок
        for column_cells in ws.columns:
            length = max(len(str(cell.value or "")) for cell in column_cells) #находим самую длинную строку в колонке для ориентира
            ws.column_dimensions[column_cells[0].column_letter].width = max(length + 2, 8) #column_dimensions - определяет букву столбца, width - присваивает ему ширину (минимум 8, +2 - запасные знаки на пробелы с двух сторон) 
        
        wb.save(xlsx_path)
        
    except FileNotFoundError:
        raise FileNotFoundError
```
### Программа для теста: 
```python
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
```
### Фото работы: До/После
<img width="756" height="712" alt="test_start" src="https://github.com/user-attachments/assets/d8d0e5f5-9c94-41dc-8ae9-2185d7643030" />
<img width="1471" height="1110" alt="test_result" src="https://github.com/user-attachments/assets/47b90fb0-cb06-4ab7-bf6f-8ad3b3cd1adb" />


## Лабораторная №6
### Подкоманды в одном CLI:
```python
import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n

def main():
    """
        1. cat   — вывод содержимого текстового файла (с нумерацией строк при флаге -n);
        2. stats — анализ частот встречаемости слов в тексте. (с указанием количества слов в топе --top n, иначе автоматически top 5)
    """

    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6") #создание парсера с описанием команд
    subparsers = parser.add_subparsers(dest="command") #dest="command" - значение выбранной команды будет храниться в args.command

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True) #required=True - обязательный элемент, хранит в себе путь к файлу
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки") #action="store_true" - флаг, который становится True если указан, иначе False

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5) #дополнительный элемент, если его нет - автоматически 5

    args = parser.parse_args() #расшифровывает введенную строку по флагам, указанным ранее

    file=Path(args.input)

    if not file.exists():
        raise FileNotFoundError("Файл не найден")


    if args.command == "cat":
        #python -m src.lab06.cli_text cat --input data/samples/test.txt -n

        with open(file, "r", encoding="utf-8") as f:
            num = 1
            for line in f:
                line = line.rstrip("\n")
                if args.n:
                    print(f"{num}: {line}")
                    num += 1
                else:
                    print(line)

    elif args.command == "stats":
        #python -m src.lab06.cli_text stats --input data/samples/test.txt --top 3

        with open(file, "r", encoding="utf-8") as f:
            data = [row for row in f]
        data = "".join(data)
    
        tokens = tokenize(data)
        freq = count_freq(tokens)
        top = top_n(freq, args.top)
    
        print(f"Топ-{args.top} слов в файле '{args.input}':")
        number = 1
        for word, count in top:
            print(f"{number}. '{word}' - {count} раз")
            number += 1

if __name__ == "__main__":
    main()
```
<img width="1261" height="639" alt="cli_text_test" src="https://github.com/user-attachments/assets/9aeb62bb-57be-4f06-a5c3-7534c054bae0" />


### CLI‑конвертер
```python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    json_to_csv_p = sub.add_parser("json2csv")
    json_to_csv_p.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    json_to_csv_p.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    csv_to_json_p = sub.add_parser("csv2json")
    csv_to_json_p.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv_to_json_p.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    csv_to_xlsx_p = sub.add_parser("csv2xlsx")
    csv_to_xlsx_p.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv_to_xlsx_p.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        #python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_from_json.csv
        json_to_csv(json_path=args.input, csv_path=args.output)

    elif  args.cmd == "csv2json":
        #python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json
        csv_to_json(csv_path=args.input, json_path=args.output)

    elif args.cmd == "csv2xlsx":
        #python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)

if __name__ == "__main__":
    main()
```
<img width="1415" height="711" alt="cli_convert_csv2json" src="https://github.com/user-attachments/assets/f021ff4b-6fcd-4241-9de8-1b3d0293a74a" />
<img width="1429" height="994" alt="cli_convert_csv2xslx" src="https://github.com/user-attachments/assets/74365074-7a74-421e-8d48-78bae7386158" />
<img width="1135" height="1042" alt="test_help" src="https://github.com/user-attachments/assets/288ff6d5-491c-470a-804e-af2731501c4d" />

##Лабораторная №7
##python -m pytest tests/test_text.py
Строка для запуска в CLI из корня папки

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

<img width="1396" height="376" alt="test_text" src="https://github.com/user-attachments/assets/4b9f434f-0615-460f-a3ad-f59c0d885694" />


##python -m pytest tests/test_json_csv.py

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
<<<<<<< HEAD
```
=======
```
<img width="1405" height="289" alt="test_json_csv" src="https://github.com/user-attachments/assets/704f873b-93f9-4803-969b-365cbfbee628" />

##black_test
<img width="870" height="372" alt="Снимок экрана 2025-11-19 160447" src="https://github.com/user-attachments/assets/dca92ff1-bbf2-4614-9c91-275ae1bf3d42" />

