#Pylones

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

pylones = []

for i in lines[1:]:
        pylones.append(int(i))


def vision(L, x):
        total = 0
        if x > 0:
                total+=1
                maxi = L[x-1]
                for j in L[x-1::-1]:
                        if j > maxi:
                                total+=1
                                maxi = j
        if x < len(L)-1:
                total+=1
                maxi = L[x+1]
                for i in L[x+1:]:
                        if i > maxi:
                                total+=1
                                maxi = i
        return total

output=''

for e, i in enumerate(pylones):
        height = vision(pylones, e)
        output+=' ' + str(height)

print(output)
