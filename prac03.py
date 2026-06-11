#Display only those characters which are present at an even index number in given string.

string = "pynative"
print(f"Original string is {string}")

for i in range(len(string[::2])):
    print(string[i])