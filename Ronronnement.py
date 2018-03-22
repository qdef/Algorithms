import sys
#lines = []
#for line in sys.stdin:
	#lines.append(line.rstrip('\n'))

#Example:
lines = ['3284493037959832844930379598']

ronron=lines[0]
N=len(ronron)
for i in range(1, N+1):
	if N%i==0 and ronron[0:i]*int(N/i)==ronron:
			print(i)
			break



