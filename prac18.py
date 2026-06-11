#Write a program to extract each digit from an integer in the reverse order.

number = 7536

while number > 0:
    digit = number % 10
    print(digit)
    number = number // 10

