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

condition = True
string = lines[1]
for i, e in enumerate(lines[0]):
	if e in string:
		string=string[string.index(e)+1:]
	else:
		condition = False
		n=i
		break

if condition:
	print('OK')
else:
	print('NOK', n)





