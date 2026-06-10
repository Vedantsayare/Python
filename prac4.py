#Write a function to remove characters from a string starting from index 0 up to n and return a new string.

def string_removal(string, i):
    return string[i:]

string = "pynative"
string = string_removal(string, 4)
print(f"String after removing first 4 characters: {string}")
string = string_removal(string, 2)
print(f"String after removing first 2 characters: {string}")