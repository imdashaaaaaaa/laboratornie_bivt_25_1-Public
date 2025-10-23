import sys
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    """
    cmd /c "python -m src.lab03.B < data/lab03/input.txt"

    echo "Привет, мир! Привет!!!" | python -m src.lab03.B 
    """

    # Чтение всего ввода из stdin
    text = sys.stdin.read()

    print(f"text {text}")
    
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