#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/

import sys
import math

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

List = lines[1:]
Bool = True

for counti, i in enumerate(List):
    a1, b1, R1 = map(int, i.split(' '))
    for countj, j in enumerate(List):
        if counti == countj :
            pass
        else:
            a2, b2, R2 = map(int, j.split(' '))
            dist = math.sqrt((a1-a2)**2 + (b1-b2)**2)
            if dist > R1 + R2:
                pass
            elif dist + min(R1, R2) < max(R1, R2):
                pass
            else:
                Bool = False
                break

print("OK" if Bool else "KO")