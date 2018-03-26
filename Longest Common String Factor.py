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

def indexes(seq, start=0):
    return (i for i,_ in enumerate(seq, start=start))

def gen_all_substrings(s):
    return (s[i:j] for i in indexes(s) for j in indexes(s[i:], i+1))

def get_all_substrings(string):
    return list(gen_all_substrings(string))

for i in lines[1:]:
    a, b = i.split(' ')
    List1 = get_all_substrings(a)
    List2 = get_all_substrings(b)
    common_list = list(set(List1).intersection(List2))
    if not common_list:
        print("AUCUN FACTEUR")
    else:
        common_list.sort()
        print(max(common_list, key=len))