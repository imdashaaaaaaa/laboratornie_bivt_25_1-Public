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
