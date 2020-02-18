# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:49:20 2020

@author: nikvi
"""

import numpy as np
import pandas as pd

print("Enter the initial state of the puzzle:")

InitialState = []
GoalState = []

for i in range(0,8):
    print("Enter the value:")
    InitialState[i] = input()
    