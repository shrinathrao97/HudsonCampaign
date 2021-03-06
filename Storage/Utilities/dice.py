import os
import math
import sys
from random import randint

#Define Roll function, generates a list of values rolled (5d6 will generate 5 rolls in a list), returns a sum of the list
def roll(numDice, numSide):

	val = ([randint(1, numSide) for i in range(numDice)])
	print (val)
	return sum(val)	



#Global control variables
cont= "y"
total = 0


#While the answer is continue keep repeating
while cont == "y":

	#Gets input to determine if the while loop should continue
	print("Enter c to clear total, q to quit, s to skillcheck, or nothing to continue")
	keepGoing = input("Enter Command: ")

	#Exit condition	
	if keepGoing == "q":
		cont = "q"	
		break
	#Clear the running total and continue	
	if keepGoing == "c":
		total = 0
	#Gets xdx values
	numDice = input("Enter number of dice: ")
	numSide = input("Enter number of sides: ")
	
	#Converts from string to int
	numDice = int(numDice)
	numSide = int(numSide)

	#Prints the current sum of roll list
	answer = roll(numDice, numSide)
	print("Your roll: ", answer)
		
	#Prints the running total of rolls so you can do things like 5d6 + 3d4
	total = total + answer
	print("Your total: ", total)
	


