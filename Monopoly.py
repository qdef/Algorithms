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

N = int(lines[0])

Values = []
for i in lines[1].split():
    Values.append(int(i))

# Creating a dictionary to store the costs of each monopoly tile:
Dico= {}
for i in range(40):
    Dico.update({i+1: Values[i]})

# Making two parallel lists to add the sums of all dice rolls:
raw_dices = lines[2].split()
dices1 = []
dices2 = []
for k in raw_dices[::2]:
    dices1.append(int(k))
for k in raw_dices[1::2]:
    dices2.append(int(k))
dices = []
for i in range(len(dices1)):
    dices.append(dices1[i] + dices2[i])

# Monopoly starts on tile 1:
case = 1
for i in dices:
    case+=i
    # The Prison case:
    if case == 20:
        case = 10
    # Going back to the beginning after 40:
    if case > 40:
        case = case - 40
    N -= Dico.get(case)
    # Print the "game over" tile:
    if N<=0:
        print(case)
        exit()

