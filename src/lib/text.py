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
    # Сначала сортируем по частоте (убывание), потом по алфавиту (возрастание)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

#if __name__ == "__main__":
#    print (normalize ("ПрИвЕт\nМИр\t"))
#    print (tokenize ("emoji 😀 не слово"))
#    print (top_n(count_freq(["a","b","a","c","b","a"]), n=2))