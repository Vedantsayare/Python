def pal(num):
    result = 0

    while num > 0:
        digit = num % 10
        result = result * 10 + digit
        num = num //10
    return result

print(pal(1234))