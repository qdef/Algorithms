"""From practicepython.org :

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
	If the number is a multiple of 4, print out a different message."""

def OddOrEven(n):
	m=abs(n)
	if m%4==0:
		return str(n) + ' is even and dividable by 4.'
	elif m%2==0:
		return str(n) + ' is an even number.'
	else:
		return str(n) + ' is an odd number.'
	

print(OddOrEven(24))
	
