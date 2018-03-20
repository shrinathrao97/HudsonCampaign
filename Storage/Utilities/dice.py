import os
import math
import sys
from random import randint

def roll(numDice, numSide):
	val = ([randint(1, numSide) for i in range(numDice)])
	print (val)
	return sum(val)	

#Have easy presets

cont= "y"
total = 0
while cont == "y":
	numDice = input("Enter number of dice: ")
	numSide = input("Enter number of sides: ")

	numDice = int(numDice)
	numSide = int(numSide)

	answer = roll(numDice, numSide)
	print("Your roll: ", answer)
		
	total = total + answer
	print("Your total: ", total)
	

	keepGoing = input("Hit enter to continue, hit c to clear total and continue, hit q to quit: ")
	
	if keepGoing == "q":
		cont = "q"	
	
	if keepGoing == "c":
		total = 0



