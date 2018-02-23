#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys

#lines = []
#for line in sys.stdin:
	#lines.append(line.rstrip('\n'))

#Example:
lines = ['20', '10', '10 12', '8 11', '11 14', '2 4', '16 12', '0 6', '9 14', '4 14', '37 20', '8 3', '8 6', '0 4', '14 6', '6 7', '1 13', '11 5', '7 17', '9 7', '12 18', '17 11']

N = int(lines[0])

T = int(lines[1])

for i in lines[2:]:
	V, U = i.split(' ')
	T-=int(V)
	T+=int(U)

print("KO" if T>0 else "OK")
