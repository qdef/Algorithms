#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/

from math import sqrt

N=int(input())

liste =[]

for i in range(N):
    liste.append(input())
for i in range(len(liste)):
    liste[i] = liste[i].split(' ')
    
sorted_list=[]

total=len(liste)

while len(sorted_list)<total:
    next_station=[]
    minimum = 1001
    for i in liste:
        k = int(i[1])
        if k < minimum:
            minimum = k
            next_station = i
    sorted_list.append(next_station)
    liste.remove(next_station)
    
liste=sorted_list

route=0

for i in range(0,len(liste)-1):
    a=(int(liste[i+1][0])-int(liste[i][0]))**2 
    b=(int(liste[i+1][1])-int(liste[i][1]))**2 
    c=(int(liste[i+1][2])-int(liste[i][2]))**2
    d=sqrt(a+b+c)
    route+=d
    
for i in range(0,len(liste)-1):
    a=(int(liste[i][0])-int(liste[i+1][0]))**2 
    b=(int(liste[i][1])-int(liste[i+1][1]))**2
    c=(int(liste[i][2])-int(liste[i+1][2]))**2
    d=sqrt(a+b+c)
    route+=d
    
route=int(route)

print(route)
