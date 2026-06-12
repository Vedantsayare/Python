#Write a program to print the first 15 terms of the Fibonacci series.

def fibonacci(n):
        a = 0
        b = 1
        for _ in range(n):
            print (a, end=" ")
            a,b = b, a+b


fibonacci(15)