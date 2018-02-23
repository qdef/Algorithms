"""
Input/Output examples:
4, FEPP, 7, FPEFPEF => -FEPP
Which makes no sense, why would you send a Fire against Fire and then Water against Plant??
4, FEPP, 5, FPFFE => +FPEP
"""


import sys

lines = ['3', 'EFF', '10', 'PPPFPFFFFE']

#/Expected output: -FEPP

N1 = int(lines[0])
Team1= lines[1]
N1 = int(lines[2])
Team2=lines[3]
Kittens1=[]
for i in Team1:
    Kittens1.append(i)
Kittens2=[]
for i in Team2:
    Kittens2.append(i)
    
# Winning rules:
def fight(x):
    if x == 'F':
        return 'E'
    if x == 'E':
        return 'P'
    if x == 'P':
        return 'F'

Attack_order = '+'
Living_kitten = False
for count, kitten in enumerate(Team2):
    print(Attack_order)
    print(Kittens1)
    print(Kittens2)
    if not Kittens2 and (Kittens1 or Living_kitten): # Player1 wins
        print(Attack_order)
        print('WIN!')
        break
    else:
        if not Kittens2 and not Kittens1 and not Living_kitten: # Both lost all their kittens:
            output='=' + Attack_order[1:]
            print(output)
            print('DRAW!')
            break
        else:
            if kitten == Attack_order[-1] and Living_kitten:  #Both kittens are of the same type: both die.
                Kittens2.remove(kitten)
                Living_kitten = False
                break
            else:
                if fight(kitten) == Attack_order[-1] and Living_kitten: #My kitten kills the following kitten.
                    Kittens2.remove(kitten)
                
        elif fight(kitten) in Kittens1:
            Living_kitten=True
            Attack_order+=fight(kitten)
            Kittens2.remove(kitten)
            Kittens1.remove(fight(kitten))
        else: # Player1 loses
            output= '-' + Attack_order[1:]
            print(output)
            print('LOSE!')
            break











