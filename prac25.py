#Write a program that takes a year as input and determines if it is a leap year.

yr = 2025

if ((yr %4 ==0 and yr %100 != 0) or yr % 400 == 0):
    print("leap year")
else:    print("not a leap year")
