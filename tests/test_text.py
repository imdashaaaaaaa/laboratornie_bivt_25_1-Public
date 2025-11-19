import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


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