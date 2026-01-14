def reverse_string(s):
    """Переворачивает строку"""
    return s[::-1]

def count_words(s):
    """Считает количество слов в строке"""
    return len(s.split())

def len_words(s):
    return len(s.split())

def is_palindrome(s):
    """Проверяет, является ли строка палиндромом"""
    clean_s = s.lower().replace(" ", "")
    return clean_s == clean_s[::-1]

# Напишите тесты для этих функций:
def test_reverse_string():
    string = "hello world"
    assert reverse_string(string) == "dlrow olleh"

def test_count_words():
    result = count_words("hello world")
    assert result == 2

def test_len_words():
    result = len_words("hello world")
    assert result == 2

def test_is_palindrome():
    result = is_palindrome("Казак")
    assert result == True