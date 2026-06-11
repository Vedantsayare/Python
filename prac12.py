#Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

def check(num: list[int]) -> bool:
    if num[0] == num[-1]:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(check(numbers_x))
print(check(numbers_y))
