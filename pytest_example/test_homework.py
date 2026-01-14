
def reverse_string(s):
    """Переворачивает строку"""
    return s[::-1]

def count_words(s):
    """Считает количество слов в строке"""
    return len(s.split())

def is_palindrome(s):
    """Проверяет, является ли строка палиндромом"""
    clean_s = s.lower().replace(" ", "")
    return clean_s == clean_s[::-1]


# Проверьте 'hello' → 'olleh'
def test_count_words():
    string = "hello"
    assert reverse_string(string) == "olleh"

# Проверьте пустую строку
def test_empty_string():
    string = ""
    assert reverse_string(string) == ""

# Проверьте одну букву
def test_character():
    string = "e"
    assert reverse_string(string) == "e"

# Проверьте 'hello world' → 2
def test_count():
    string = "hello world"
    assert count_words(string) == 2

# Проверьте пустую строку
def test_empty_count():
    string = ""
    assert count_words(string) == 0

# Проверьте одно слово
def test_one_word():
    string = "hello"
    assert count_words(string) == 1

# Проверьте 'racecar' → True
def test_palindrome():
    string = "racecar"
    assert is_palindrome(string) == True

# Проверьте 'A man a plan a canal Panama'
def test_palindrome2():
    string = "A man a plan a canal Panama"
    assert is_palindrome(string) == True

def test_palindrome3():
    string = "hello"
    assert is_palindrome(string) != True

