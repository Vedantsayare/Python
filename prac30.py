#Given a number, apply the Collatz rule (if even, divide by 2; if odd, multiply by 3 and add 1) repeatedly until you reach 1. Count and return how many steps it took.

def collatz(num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            print(num)
        else :
            num = (num * 3) + 1
            print(num)
        steps += 1
    return steps

num = int(input("Enter number:"))
if num <= 0:
    print("Invalid input!")
else:
    steps = collatz(num)
    print(f"return to 1 in {steps} steps")