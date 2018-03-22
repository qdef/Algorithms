#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def crypt(x):
	if x == ' ':
		return ' '
	if x.isdigit():
		return x
	x=x.lower()
	if x =='a' or x=='j':
		return '1'
	elif x=='b' or x=='k' or x=='s':
		return '2'
	elif x=='c' or x=='l' or x=='t':
		return '3'
	elif x=='d' or x=='m' or x=='u':
		return '4'
	elif x=='e' or x=='n' or x=='v':
		return '5'
	elif x=='f' or x=='o' or x=='w':
		return '6'
	elif x=='g' or x=='p' or x=='x':
		return '7'
	elif x=='h' or x=='q' or x=='y':
		return '8'
	elif x=='i' or x=='r' or x=='z':
		return '9'

ribs = []

for i in lines:
	rib = ''
	for j in i:
		rib+=crypt(j)
	ribs.append(rib)


local_print(lines)
local_print(ribs)

for i in ribs:
	values = i.split(' ')
	total = 89*int(values[0]) + 15*int(values[1]) + 3*int(values[2])
	key = 97 - total%97
	local_print(key)
	if key == int(values[3]):
		print('OK')
	else:
		print('KO')
