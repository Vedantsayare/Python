def iterate(i):
    if i == 0:
        print(f"Current number {i}, previous number {i},sum : {i}")
    else:        
        print(f"Current number {i}, previous number {i-1},sum : {i +(i-1)}")

numbers= range(10)

print("printing sum of current and previous number in range 10")
for i in numbers:
    iterate(i)