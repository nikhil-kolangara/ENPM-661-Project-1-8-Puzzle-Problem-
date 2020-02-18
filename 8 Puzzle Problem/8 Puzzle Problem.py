# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:49:20 2020

@author: nikvi
"""

import numpy as np
import pandas as pd

print("Enter the initial state of the Puzzle:")

initialState = []
goalState = []

for i in range(0,9):
    print("Enter the value:")
    value = int(input())
    initialState.append(value)