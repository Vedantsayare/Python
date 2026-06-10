#Given a list of integers, find and print both the largest and the smallest numbers

nums = [45, 2, 89, 12, 7]

min = nums[0] 
max = nums[0]

for num in nums:
    if num < min:
        min = num
    if num > max:
        max = num

print(f"Minimum value in the list is: {min}")
print(f"Maximum value in the list is: {max}")