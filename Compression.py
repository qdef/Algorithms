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

List = lines[0]

output = ''
for e, i in enumerate(List):
    if e > 0 and List[e]==List[e-1]:
        pass
    else:
        count = 0
        for k in List[e:]:
            if k == i:
                count+=1
            else:
                break
        if count == 1:
            output+= i
        elif count == 2:
            output+= i+i
        elif count>2:
            output+= str(count)+i 

local_print(List)
print(output)

