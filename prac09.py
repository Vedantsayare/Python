#Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

sentence = "Learning Python is fun!"
vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
count = 0

for char in sentence:
    if char in vowel:
        count += 1

print(f"Total number of vowels in the sentence is: {count}")