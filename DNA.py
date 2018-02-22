#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys
import itertools

"""for line in sys.stdin:
	lines.append(line.rstrip('\n'))"""
	
lines = ['7', 'T', 'GTAGA', 'CGCA', 'GAC', 'GCGT', 'CTGC', 'ATC']

# The DNA rule:
def complementary(x):
	if x == 'A':
		return 'T'
	elif x == 'T':
		return 'A'
	elif x == 'C':
		return 'G'
	elif x == 'G':
		return 'C'

N = int(lines[0])
fragments = lines[1:]

#What is the total length of the chromosome?
total_bp = 0
for i in fragments:
	for j in i:
		total_bp+=1
chromosome_length = int(total_bp/2)

# Assembling all DNA fragments that fit the chromosome size:
fragment_combinations = []
for i in range(0, N+1):
	for j in itertools.permutations(fragments, i):
		dna = ' '.join(j)
		packed_dna = dna.replace(' ', '')
		if len(packed_dna)==chromosome_length:
			fragment_combinations.append(dna)

# Selecting fragments that have a reverse complement :
comp_fragments = []
for dna1 in fragment_combinations:
	dna_list1=dna1.split()
	packed_dna = dna1.replace(' ', '')
	reverse = ''
	for nucleotide in packed_dna :
		reverse += complementary(nucleotide)
	for dna2 in fragment_combinations:
		dna_list2=dna2.split()
		packed_dna2 = dna2.replace(' ', '')
		if reverse==packed_dna2 and len(dna_list1)+len(dna_list2) == N :
			if dna2 not in [comp_fragments[i] for i in range(len(comp_fragments))]:
				comp_fragments.append(dna1)
				comp_fragments.append(dna2)

crick = comp_fragments[0]
watson = comp_fragments[1]

# In case you didn't know, on any chromosome, there is always one strand called Crick and the other one called Watson.
sequence = crick + '#' + watson
print(sequence)
