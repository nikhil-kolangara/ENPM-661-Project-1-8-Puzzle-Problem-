# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:49:20 2020

@author: nikvi
"""

import numpy as np
import os
import copy as cp
import sys
        
actionList = ["left", "right", "up", "down"]

nodeList = []
valueList = []
nodePath = []


class newNode:
    def __init__(self, nodeNumber, data, parent):
        self.nodeNumber = nodeNumber
        self.data = data
        self.parent = parent

def inputNode():
    print("Enter the initial state of the Puzzle:")

    initialState = []
    for i in range(3):
        for j in range(3):
            print("Enter the value:")
            value = int(input())
            if (value > 8) or (value < 0):
                print("Please enter values between 0 to 8")
            else: 
                initialState.append(int(value))
    
    return initialState
    
def isSolvable(iS):
    solvable = iS #np.reshape(iS,9)
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
        
def isCorrect(iC):
    correct = iC #np.reshape(iC, 9)
    for i in range(9):
        count = 0
        cvalue = correct[i]
        for j in range(9):
            if cvalue == correct[j]:
                count = count + 1
        if count >= 2:
            print("Number inputted Twice, Cannot Proceed!")
            exit(0)
  
def blankTileLocation(iN):
    initialNode = iN #np.reshape(iN, 9)
    for i in range (9):
            if initialNode[i] == 0:
                break
    return i     

def isRepeating(val):
    try:
        x = valueList.index(val)
        return True
    except:
        return False
    
def actionMoveLeft(currentNode):
    i = blankTileLocation(currentNode.data)
    newData = cp.deepcopy(currentNode.data)
    if(i == 0 or i == 3 or i == 6):
        return None
    else:
        temp = newData[i-1]
        newData[i-1] = newData[i]
        newData[i] = temp
        if(isRepeating(newData) == False):
            valueList.append(newData)
            nodeList.append(newNode(0, newData, currentNode))
    
def actionMoveRight(currentNode):
    i = blankTileLocation(currentNode.data)
    newData = cp.deepcopy(currentNode.data)
    if(i == 2 or i == 5 or i == 8):
        return None
    else:
        temp = newData[i+1]
        newData[i+1] = newData[i]
        newData[i] = temp
        if(isRepeating(newData) == False):
            valueList.append(newData)
            nodeList.append(newNode(0, newData, currentNode))
    
def actionMoveUp(currentNode):
    i = blankTileLocation(currentNode.data)
    newData = cp.deepcopy(currentNode.data)
    if(i == 0 or i == 1 or i==2):
        return None
    else:
        temp = newData[i-3]
        newData[i-3] = newData[i]
        newData[i] = temp
        if(isRepeating(newData) == False):
            valueList.append(newData)
            nodeList.append(newNode(0, newData, currentNode))
    
def actionMoveDown(currentNode):
    i = blankTileLocation(currentNode.data)
    newData = cp.deepcopy(currentNode.data)
    if(i == 6 or i == 7 or i == 8):
        return None
    else:
        temp = newData[i+3]
        newData[i+3] = newData[i]
        newData[i] = temp
        if(isRepeating(newData) == False):
            valueList.append(newData)
            nodeList.append(newNode(0, newData, currentNode))

def moveBlankTile(action, currentNode):
    if action == 'left':
        return actionMoveLeft(currentNode)
    if action == 'right':
        return actionMoveRight(currentNode)
    if action == 'up':
        return actionMoveUp(currentNode)
    if action == 'down':
        return actionMoveDown(currentNode)
    else:
        return None

def columnWise(nodedata):
    colData = []
    for i in range(3):
        for j in range(i,9,3):
            colData.append(str(nodedata[j]))
    return " ".join(colData)#' '.join([str(elem) for elem in colData]) 

def solvePuzzle(startNode):
    print("Solving...")
    actionList = ['left', 'right', 'up', 'down']
    #goalState = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    goalState = [1,2,3,4,5,6,7,8,0]
    nodeList.append(startNode)
    valueList.append(startNode.data)
    file_nodes = open("nodes.txt","w")
    file_nodeInfo = open("nodeInfo.txt","w")
    file_nodePath = open("nodePath.txt","w")
    #nodeCounter = 0 
    
    for node in nodeList:
        try:
            file_nodeInfo.write(str(valueList.index(node.data)+1)+" "+str(valueList.index(node.parent.data)+1)+" 0")
            file_nodeInfo.write("\n")
        except: #no Parent Case
            file_nodeInfo.write(str(valueList.index(node.data)+1)+" 0 0")
            file_nodeInfo.write("\n")
        
        file_nodes.write(columnWise(node.data))
        file_nodes.write("\n")
        if goalState == node.data:
            print("found solution")
            break
        else:
            for action in actionList:
                moveBlankTile(action, node)
        
    try:
        index = valueList.index(goalState)
        print("found the solution at%d"%index)
        while index != 0:
            nodePath.append(index)
            parentValueAt = nodeList[index].parent.data
            index = valueList.index(parentValueAt)
        nodePath.append(0) #adding the startNode
        
        for i in reversed(nodePath):
            file_nodePath.write(columnWise(valueList[i]))
            file_nodePath.write("\n")
            
        
            
    except:
        sys.exit()

    file_nodes.close()
    file_nodePath.close()
    file_nodeInfo.close()
                

initialState = inputNode()
isCorrect(initialState)
isSolvable(initialState)
rootNode = newNode(0, initialState, None)
solvePuzzle(rootNode)
