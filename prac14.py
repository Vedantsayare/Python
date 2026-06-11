#Write a program to find how many times the substring “Emma” appears in a given string.

stri = "Emma is good developer. Emma is a writer"
count = 0
words = stri.split()
for word in words:
    if word == "Emma":
        count += 1
print(count)