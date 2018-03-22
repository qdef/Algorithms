#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys
import math
from datetime import datetime
import time

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

distances=[]
for i in lines:
	values = i.split(' ')
	distances.append([int(values[0]), int(values[1])])

total_dist = 0
for i, value in enumerate(distances):
	if i==0:
		pass
	else:
		absc = (distances[i][0]-distances[i-1][0])**2
		ordo = (distances[i][1]-distances[i-1][1])**2
		total_dist += math.sqrt(absc+ordo)/1000

departure = lines[0].split(' ')[2]
arrival = lines[len(lines)-1].split(' ')[2]
d1 = datetime.strptime(departure, "%H:%M:%S")
d2 = datetime.strptime(arrival, "%H:%M:%S")

total_time = (d2 - d1).seconds/3600
avg_speed = total_dist/total_time

print(round(avg_speed,2))