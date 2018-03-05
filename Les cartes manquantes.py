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
cards = lines[0]
deck = cards.split(' ')

coeur = []
pique = []
carreau = []
trefle = []

for i in deck:
	if i[0]=='C':
		coeur.append(i[1:])
	if i[0]=='P':
		pique.append(i[1:])
	if i[0]=='Q':
		carreau.append(i[1:])
	if i[0]=='T':
		trefle.append(i[1:])

total = ['2','3','4','5','6','7','8','9','10','V','D','R','A']

sorted_coeur = []
sorted_pique = []
sorted_carreau = []
sorted_trefle = []

for i in total:
	if i in coeur:
		sorted_coeur.append(i)

for i in total:
	if i in pique:
		sorted_pique.append(i)

for i in total:
	if i in carreau:
		sorted_carreau.append(i)

for i in total:
	if i in trefle:
		sorted_trefle.append(i)

output=''

for i in total:
	if i not in sorted_coeur:
		output+='C'+i+' '

for i in total:
	if i not in sorted_pique:
		output+='P'+i+' '

for i in total:
	if i not in sorted_carreau:
		output+='Q'+i+' '

for i in total:
	if i not in sorted_trefle:
		output+='T'+i+' '

print(output)