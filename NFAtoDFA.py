# -*- coding: utf-8 -*-
# Define the NFA
# A = q0, B = q1, C = q2, D = q3, E = q4, F = q5
NULL = 'Ø'

NFA={'A':{'a':['A','B','D']}, #q0 = 'A'
     'B':{'a':['C']},
     'C':{'a':['B']},
     'D':{'a':['E']},
     'E':{'a':['F']},
     'F':{'a':['D']}}

#Examples
NFA1={'A':{'0':['A','B'],'1':['A']}, #q0 = 'A'
    'B':{'0':[NULL],'1':['C']},
    'C':{'0':[NULL],'1':[NULL]}}

NFA2={'A':{'a':['B'],'b':[NULL]}, #q0 = 'A'
    'B':{'a':['B'],'b':['A']},
    'C':{'a':[NULL],'b':['A']}}

NFA3={'A':{'a':['B','C'],'b':['B','D'],'c':['C','D']}, #q0 = 'ABCD'
    'B':{'a':['B'],'b':['B'],'c':[NULL]},
    'C':{'a':['C'],'b':[NULL],'c':['C']},
    'D':{'a':[NULL],'b':['D'],'c':['D']}}

NFA4={'A':{'a':['A','B','C','D','E','F'],'b':['A','C','D','E']}, #q0 = 'AC'
    'B':{'a':['A','C','D','E','F'],'b':['C']},
    'C':{'a':['A','C','D','E','F'],'b':[NULL]},
    'D':{'a':['A','B','C','D','E','F'],'b':['A','C','D','E']},
    'E':{'a':['A','B','C','D','E','F'],'b':['A','C','D','E']},
    'F':{'a':['A','B','C','D','E','F'],'b':['A','C','D','E']}}

NFA5={'A':{'a':['B','C'],'b':[NULL]}, #q0 = 'A'
    'B':{'a':['B','C'],'b':['A']},
    'C':{'a':[NULL],'b':['A']}}

NFANULL={'A':{'a':[NULL]}}

NFALOOP = {'A':{'a':['A']}}

#manually change this to choose which NFA to test
currentTest = NFA1
q0 = 'A'
#make sure to manually change this to fit the current NFA based on its q0 lambda transitions
#q0 for above examples are listed 
        
# Define the DFA
from collections import OrderedDict
DFA = OrderedDict()

print("\nConverting following NFA to DFA:")
print(currentTest)

# add the initial state to the DFA
valsToCheck = ["empty",q0]#list would diappear if i popped the last element off, instead taking from end and leaving "empty" as a flag
DFA[q0] = {}

# Algorithm
checkedVals = [q0]
temp3 = ''
done=False
currVal =''
hardstop = 0 

for keyCheck1, valueCheck1 in DFA.items():#initial check to see if q0 loops to only itself
    if currVal == keyCheck1 and len(valsToCheck) == 1:
        done=True
        break
if done:
    print("init value loops on itself only")

while not done and hardstop<100:#loop start, increase hardstop if necessary for a large DFA
    currVal = valsToCheck.pop(len(valsToCheck)-1)
    DFA[currVal] = {}
    
    for key1, value1 in currentTest.items():
        for key2, value2 in value1.items():
            if key2 not in DFA[currVal]: #adding areas for each symbol
                DFA[currVal][key2] = ""
    
    for element in range(0,len(currVal)):
        for key, value in currentTest.items():
            if currVal[element] in key:
                for keySymbol, valueResult in value.items():
                    for val in valueResult:
                        if val not in temp3 and val is not NULL and val not in DFA[currVal][keySymbol]:#ignoring trap states
                            temp3+=val
                    DFA[currVal][keySymbol] += temp3
                    temp3 = ''
                    
    #adding trap state if necessary
    for key, value in DFA[currVal].items():
        if value == '':
            DFA[currVal][key] = NULL
           
    #checking if there are new nodes to check
    checkedVals.append(currVal)
    keyCheck = DFA.keys()
    for key, value in DFA[currVal].items():
        for val in value:
            if val not in valsToCheck and val not in keyCheck and value not in checkedVals:
                valsToCheck.append(value)
                break
        
    if len(valsToCheck) == 1:
        done=True
        break
    
    hardstop +=  1
    
# Display the result
print("\nCompleted, the converted DFA is:")
print(DFA) 
