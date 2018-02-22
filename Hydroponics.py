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

N= int(lines[0])
lines = lines[1:]

#Count the number of evaporators (X):
x_count=0
for i in lines:
	for j in i:
		if j=="X":
			x_count+=1

#Add an empty zone around the field:
lanes = ['.'+ i + '.' for i in lines]
horizontal = [(N+2) * '.']
field = horizontal + lanes + horizontal

# Determines if the coordinate is in the field:
def isinfield(x):
	if x in range(len(lines)):
		return True
	return False

watercount=set()

for i in range(1, N+1):
	for j in range(1, N+1):
		if field[i][j] == 'X':
			for k in [i-2, i-1, i]:
				for l in [j-2, j-1, j]:
					if isinfield(k) and isinfield(l):
						watercount.add((k,l))
						
total= len(watercount) - x_count
print(total)