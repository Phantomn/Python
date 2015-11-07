#!/usr/bin/python
import os
number = 23
guess = int(input("Enter an integer : "))
if guess == number:
	print("Congratulations, you guessed it.\n(but you do not win any prizes!")
	exit()
elif guess < number:
	print("No, it is little higher than that")
else:
	print("No, it is a little lower than that")
print("Done")