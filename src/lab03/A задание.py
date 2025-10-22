import re
from collections import Counter


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализация текста"""
    if not text:
        return ""
    
    # Замена ё на е если нужно
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    # Приведение к casefold если нужно
    if casefold:
        text = text.casefold()
    
    # Замена невидимых управляющих символов на пробелы
    # \t, \r, \n и другие пробельные символы
    text = re.sub(r'[\t\r\n\v\f]', ' ', text)
    
    # Схлопывание повторяющихся пробелов и удаление пробелов по краям
    text = re.sub(r' +', ' ', text).strip()
    
    return text


def tokenize(text: str) -> list[str]:
    """Разбиение текста на токены"""
    if not text:
        return []
    
    # Используем регулярное выражение для поиска слов
    # \w+ (буквы/цифры/подчёркивание) плюс слова с дефисами внутри
    pattern = r'\b[\w]+(?:-[\w]+)*\b'
    tokens = re.findall(pattern, text)
    
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчет частот токенов"""
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Топ-N токенов по частоте"""
    if not freq:
        return []
    
    # Сортируем сначала по убыванию частоты, затем по алфавиту
    sorted_items = sorted(
        freq.items(),
        key=lambda x: (-x[1], x[0])  # - для убывания частоты, обычный порядок для строк
    )
    
    return sorted_items[:n]


# Тестирование
if __name__ == "__main__":
    # Тесты для normalize
    print("=== normalize ===")
    print(repr(normalize("ПрИвЕт\nМИр\t")))  # "привет мир"
    print(repr(normalize("ёжик, Ёлка")))  # "ежик, елка"
    print(repr(normalize("Hello\r\nWorld")))  # "hello world"
    print(repr(normalize("  двойные   пробелы  ")))  # "двойные пробелы"
    
    # Тесты для tokenize
    print("\n=== tokenize ===")
    print(tokenize("привет мир"))  # ["привет", "мир"]
    print(tokenize("hello,world!!!"))  # ["hello", "world"]
    print(tokenize("по-настоящему круто"))  # ["по-настоящему", "круто"]
    print(tokenize("2025 год"))  # ["2025", "год"]
    print(tokenize("emoji 😀 не слово"))  # ["emoji", "не", "слово"]
    
    # Тесты для count_freq + top_n
    print("\n=== count_freq + top_n ===")
    tokens1 = ["a", "b", "a", "c", "b", "a"]
    freq1 = count_freq(tokens1)
    print(freq1)  # {"a":3,"b":2,"c":1}
    print(top_n(freq1, 2))  # [("a",3), ("b",2)]
    
    tokens2 = ["bb", "aa", "bb", "aa", "cc"]
    freq2 = count_freq(tokens2)
    print(freq2)  # {"aa":2,"bb":2,"cc":1}
    print(top_n(freq2, 2))  # [("aa",2), ("bb",2)]