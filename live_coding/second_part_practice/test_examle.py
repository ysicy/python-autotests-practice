def test_one():
    num = '12345'
    a = num[:2]
    b = num[2:][::-1]
    print(a+b)