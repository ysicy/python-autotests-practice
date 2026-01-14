def check_palindrome(s: str) -> bool:
    text = s.lower().replace(" ", "")
    return text == text[::-1]



check_palindrome("Казак")
check_palindrome("")
check_palindrome('123')
check_palindrome('123321')
check_palindrome('dad')

def check_one_word_for_slicing(s):
    return print(s[6:])

check_one_word_for_slicing("catandapple") #apple

def lucky_number(number):
    left_digits = sum([int(d) for d in number[:3]])
    right_digits = sum([int(d) for d in number[3:]])

    if left_digits==right_digits:
        print("lucky number")
    else:
        print("not lucky number")

lucky_number("123222")
lucky_number("235864")

print(True+4) #5


