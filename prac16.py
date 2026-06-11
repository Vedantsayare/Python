# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

def pa(n):
    n = str(n)

    if n == n[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number isn't a palindrome.")

pa(12321)
pa(1256)