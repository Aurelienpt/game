# Crazy game ordered by Nuf
from random import randrange
print("Game start")
nombre = randrange(1, 100)
i = 0
while i != 7:
	proposition = input("Try to find the good number between 1 and 100 : ")
	if proposition == nombre:
		print("You just win ! Answer :", nombre)
		exit()
	elif proposition > nombre:
		print(proposition, ": Smaller !")
	else:
		print(proposition, ": Higher !")
	i += 1
print("End of the game, you lose :(")