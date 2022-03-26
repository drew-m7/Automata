# -*- coding: utf-8 -*-
# This python program takes a DFA and minimizes it to its optimal state
import numpy as np

# Define the DFA by defining its transition table
DFA = {0:{'a':1,'b':2}, 1:{'a':1,'b':1}, 2:{'a':1,'b':3},
      3:{'a':4,'b':5}, 4:{'a':4,'b':6}, 5:{'a':7,'b':8},
      6:{'a':7,'b':8}, 7:{'a':9,'b':10},8:{'a':7,'b':11},
      9:{'a':1,'b':10},10:{'a':7,'b':12},11:{'a':7,'b':13},
      12:{'a':7,'b':11},13:{'a':14,'b':13},14:{'a':15,'b':10},15:{'a':4,'b':10}}

print("\nConverting the following DFA to minimized DFA:\n")
print(DFA)

sigma = ['a','b']

# Make key pairs
keys = [(i,j)  for i in range(16) for j in range(i+1, 16)]

# Make the table
table = np.zeros((16,16))
tableCheck = np.zeros((16,16))

# Make the 0-equivilence  
final_set = {2,4,5,6,7,8,9,10,11,12,13,14,15}

for a,b in keys:
    if (a in final_set) + (b in final_set) == 1 :
        table[a,b] = 1
        table[b,a] = 1

# The algorithm
# Repeat the following process until no new m[p, q] is set to 1
# For every p, q ∈ Q with p ≠ q and m[p, q] = 0
# If there exists a ∈ Σ such that m[δ(p, a), δ(q, a)]=1
# Then set m[p, q]=m[q, p]=1
# --------------
# For each a, b in keys, where no a=b and table[a,b] = 0
# If there exists x ∈ Σ such that table[δ(a, x), δ(b, x)]=1
# Set a,b and b,a to 1
eq = False;

while not eq:
    tableCheck = table.copy();
    
    
    for a,b in keys:
        if a != b and table[a,b] == 0:
            # If there exists x ∈ Σ such that table[δ(a, x), δ(b, x)]=1
            for i in range(len(sigma)): 
                x = DFA[a][sigma[i]]
                y = DFA[b][sigma[i]]
                
                if table[x,y] == 1: 
                    table[a,b] = 1
                    table[b,a] = 1
            
    if(np.array_equal(table,tableCheck)):
        print("\nTrue\n");
        eq = True;

# Output the minimized solution table
print("\nThe minimized DFA as a table(matrix):\n")
print(table)
