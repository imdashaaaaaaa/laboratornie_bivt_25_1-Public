import re
import sys
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
    text = re.sub(r'[\t\r\n\v\f]', ' ', text)
    
    # Схлопывание повторяющихся пробелов и удаление пробелов по краям
    text = re.sub(r' +', ' ', text).strip()
    
    return text


def tokenize(text: str) -> list[str]:
    """Разбиение текста на токены"""
    if not text:
        return []
    
    # Используем регулярное выражение для поиска слов
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
        key=lambda x: (-x[1], x[0])
    )
    
    return sorted_items[:n]


def main():
    # Чтение всего ввода из stdin
    text = sys.stdin.read()
    
    # Нормализация текста
    normalized_text = normalize(text, casefold=True, yo2e=True)
    
    # Токенизация
    tokens = tokenize(normalized_text)
    
    # Подсчет статистики
    total_words = len(tokens)
    unique_words = len(set(tokens))
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, n=5)
    
    # Вывод результатов
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()