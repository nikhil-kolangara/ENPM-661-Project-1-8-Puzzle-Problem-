# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:49:20 2020

@author: nikvi
"""

import numpy as np
import pandas as pd

print("Enter the initial state of the Puzzle:")

initialState = []
goalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]

for i in range(0,9):
    print("Enter the value:")
    value = int(input())
    initialState.append(value)
    
print(initialState)

for i in range(0,len(initialState)):
    for j in range(0, len(initialState) - i - 1):    
        if initialState[j] > initialState[j+1]:
            temp = initialState[j]
            initialState[j] = initialState[j+1]
            initialState[j+1] = temp
        
print(initialState)
        