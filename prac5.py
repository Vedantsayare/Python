#Write a program to swap the values of two variables, a and b, without using a third temporary variable.

def swap(a, b):
    return b,a

print("Enter two numbers to swap:")
num1 = int(input("Enter first number: "))   
num2 = int(input("Enter second number: "))
num1, num2 = swap(num1, num2)

print(f"After swapping: num1 = {num1}, num2 = {num2}")