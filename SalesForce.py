import sys

lines = ['15', '12', '4', '10', '11', '5', '3', '7', '22', '5', '8', '9', '7', '8']

L=int(lines[0]) #Max space on each floor
Teams = []
for i in lines[2:]:
	Teams.append(int(i))
Full_Floors=0

#Removing teams that are too big and adding teams that exactly fit the floor size:
for i in Teams[::-1]:
	if i > L:
		Teams.remove(i)
	elif i==L:
		Full_Floors+=1
		Teams.remove(i)

# This function couples teams that fit a whole floor (2 teams max per floor)
def assembly(x,f,b):
	for counti, i in enumerate(x):
		for countj, j in enumerate(x):
			if i+j == L and counti != countj: #Do not use the same team twice
				f+=1  #One additional floor has been filled!
				x.pop(counti)
				if counti<countj: #Gotta be careful with the positions in the list before removing the second team!
					x.pop(countj-1) 
				else:
					x.pop(countj)
				return x, f, True
	# Switches boolean to False if the function did not find any teams left to match:
	return x, f, False 

boolean = True
while boolean:
	Teams, Full_Floors, boolean = assembly(Teams,Full_Floors,boolean)

print(Full_Floors)
