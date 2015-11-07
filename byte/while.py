number = 23
running = True

while running:
	guess = int(input("Enter an integer : "))
	if guess == number:
		print("Congratulations, you guessed it.\n(but you do not win any prizes!)")
		running = False
	elif guess < number:
		print("No, it is little higher than that")
	else:
		print("No, it is a little lower than that")
print("Done")
