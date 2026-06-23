#Find the second largest number in a list without using sort() or max() twice naively (handle duplicates correctly).

def sec_lar(numbers):
    highest = float("-inf")
    sec_highest = float("-inf")

    for i in numbers:
        if i > highest:
            sec_highest = highest
            highest = i
        elif highest > i > sec_highest:
            sec_highest = i

    return sec_highest

numbers = [23,45,89,9,80,67]
sec = sec_lar(numbers)
print(f"second largest from {numbers} -> {sec}")