#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

def calculate(a,b):
    prod = a*b

    if prod <= 1000:
        return prod
    else:        
        return a+b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate(num1 , num2)
print(f"The result is: {result}")