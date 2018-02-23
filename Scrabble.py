#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys
from string import ascii_uppercase

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
values=lines[1].split(' ')

words=[]
for i in lines[2:]:
	words.append(i)

letters=[]
for i in ascii_uppercase:
	letters.append(i)

dico={}
for count, i in enumerate(values):
	dico.update({letters[count]: i})

dico2={}
for word in words:
	count=0
	for j in word:
		count+=int(dico.get(j))
	dico2.update({word: count})

maxi=0
for key, value in dico2.items():
	if value>maxi:
		maxi = value
	
best_words=[]
for key, value in dico2.items():
	if value == maxi:
		best_words.append(key)
		
if len(best_words)==1:
	print(maxi, len(best_words[0]))
else:
	mini=float('inf')
	for i in best_words:
		if len(i)<mini:
			mini=len(i)
	print(maxi, int(mini))