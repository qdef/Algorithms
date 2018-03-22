""" From practicepython.org :

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""

import datetime

def age():
	name = str(input('What is your name?\n'))
	age = input('What is your age?\n')
	repeats=input('How many repetitions would you like?\n')
	now = datetime.datetime.now()
	answer = str(now.year - int(age) + 100 - 1)
	for i in range(int(repeats)):
		print(name + ' will reach 100 years old in ' + answer + '.')
age()



