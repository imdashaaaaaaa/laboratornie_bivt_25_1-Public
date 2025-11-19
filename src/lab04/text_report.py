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
norm_p = normalize(p)
tokens = tokenize(norm_p)
count_word = count_freq(tokens)
top = top_n(count_word)

write_csv(top, output_path, ["word", "count"])

print("Всего слов:", len(tokens))
print("Уникальных слов:", len(count_word))
print("Топ-5:")
for x, y in top[:5]:
    print(f"{x}:{y}")
