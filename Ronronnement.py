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

ronron=lines[0]
local_print(ronron)
N=len(ronron)

pattern_list=[]
for i in range(1, N+1):
	if N%i==0:
		pattern = ronron[0:i]
		local_print(pattern*int(N/i))
		if pattern*int(N/i)==ronron:
			print(i)
			break



