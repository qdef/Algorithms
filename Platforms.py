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

# Input example:
lines = ['23', '_-______----____----_-_']

N = int(lines[0])
ground = lines[1]

maximum = 0
if "_" not in ground:
	print(1)
else:
	for count, i in enumerate(ground):
		if i == "_":
			cluster = 1
			for j in ground[count+1:]:
				if j=='_':
					cluster+=1
				else:
					break
			if cluster>maximum:
				maximum=cluster
	maximum+=1
	print(maximum)


