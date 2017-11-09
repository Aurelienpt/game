# Crazy game ordered by Nuf
from random import randrange
print("Game start")
nombre = randrange(1, 100)
i = 0
while i != 7:
	proposition = raw_input("Try to find the good number between 1 and 100 : ")
	try:
		proposition = int(proposition)
	except ValueError:
			print(str(proposition) + " is not a valid number")
			continue
	if isinstance(proposition, int):
		if proposition == nombre:
			print("You just win ! Answer :", nombre)
			exit()
		elif proposition > nombre:
			print(str(proposition) + " : Smaller !")
		else:
			print(str(proposition) + " : Higher !")
		i += 1
	else:
		print(str(proposition) + " is not a valid number")
print("End of the game, you lose :(")