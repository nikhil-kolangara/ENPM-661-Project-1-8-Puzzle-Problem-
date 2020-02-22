# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:49:20 2020

@author: nikvi
"""

import numpy as np

print("Enter the initial state of the Puzzle:")

initialState = []
a = []
goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

for i in range(3):
    for j in range(3):
        print("Enter the value:")
        a.append(int(input()))
    initialState.append(a)
        
initialState = np.transpose(initialState)
print(initialState)

def blankTileLocation(initialState):
    for i in range (3):
        for j in range(3):
            if initialState[i][j] == 0:
                break
    return(i,j)
            
[i,j] = blankTileLocation()
print(i,j)
    
#print(initialState)
"""
for i in range(0,len(initialState)):
    for j in range(0, len(initialState) - i - 1):    
        if initialState[j] > initialState[j+1]:
            temp = initialState[j]
            initialState[j] = initialState[j+1]
            initialState[j+1] = temp
        
print(initialState)
"""


        