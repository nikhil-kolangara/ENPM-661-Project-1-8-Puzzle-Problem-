# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:49:20 2020

@author: nikvi
"""

import numpy as np

# structure to store parameters

class Node:
    def __init__(self, node_no, data, parent, act, cost):
        self.data = data
        self.parent = parent
        self.act = act
        self.node_no = node_no
        self.cost = cost

def initialNode():
    print("Enter the initial state of the Puzzle:")
    initialState = []
    userInput = []
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    for i in range(3):
        for j in range(3):
            print("Enter the value:")
            value = int(input())
            if (value > 8) or (value < 0):
                print("Please enter values between 0 to 8")
            else: 
                userInput.append(int(input()))
                initialState.append(userInput)
        
    initialState = np.transpose(initialState)
    print(initialState)
    
def isSolvable(initialState):
    solvable = initialState
    count = 0
    for i in range(9):
        if solvable[i] != 0:
            value = solvable[i]
            for j in range(i + 1, 9):
                if value < solvable[j] or solvable[j] == 0:
                    continue
                else:
                    count = count + 1
    if (count % 2) == 0:
        print("The Puzzle is solvable.")
    else:
        print("The puzzle is insolvable.")
        
def isCorrect(initialState):
    correct = initialState
    for i in range(9):
        count = 0
        value = array[i]
        for j in range(9):
            if value == array[j]:
                count = count + 1
        if count >= 2:
            print("Number inputted Twice, Cannot Proceed!")
            exit(0)

    



def actionMoveLeft(initialState):
    if((initialState[i] != 0) && initialState[j] != 0,1,2):
        
    
def actionMoveRight(initialState):
    if((initialState[i] != 0,1,2) && initialState[j] != 2):
        
    
def actionMoveUp(initialState):
    if((initialState[i] != 0) && (initialState[j] != 0)):
        initialState[i-1][j] = initialState[i][j]
    
def actionMoveDown(initialState[i]):
    if((initialState[i] != 2) && (initialState[j] != 2):
        initialState[i+1][j] = initialState[i][j]
        

def blankTileLocation(initialState):
    for i in range (3):
        for j in range(3):
            if initialState[i][j] == 0:
                break
    return(i,j)
            
[i,j] = blankTileLocation()
print(i,j)
    


        