# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import graphics.graphics as gra
import numpy as np

def readCSV(fileName):
    #arrays of inputs  last line 
    #would be target like 
    #data mining
    #2)
    dataArr = []
    
    #nice visualization
    return dataArr

dataArr = np.asarray([np.array([1,2,1]),np.array([-1,2,0]),np.array([0,-1,0])]).astype('float')

def perceptronTrainingAlgh(dataArr):
    #1) know how much weights my model have
    #collums are the number off weights n-1
    inputsLastIndex = len(dataArr[0])-1
     
    #2)initialize weights
    weightInicialization = ((np.random.rand(1,len(dataArr[1])-1)*2)-1).ravel()
#    weightInicialization = np.zeros((1,len(dataArr[1])-1)).ravel().astype("int")
    oldWeight = weightInicialization.copy()
    newWeight = weightInicialization.copy()
    
#    oldB = np.zeros((1,len(dataArr[1])-1)).ravel()
#    newB = oldB  
    n=0

#    initial state not converged flag
    converge = False
    while not converge:
        #assume that will converge
        converge = True
        for sample in dataArr:
#            sample have point and class belonging
#           sample = [-1, 2, 0]       
            inputs = np.asarray(sample[:inputsLastIndex])
#            class
            last = -1
            target = sample[last]
            
#            n = np.sum(np.dot(inputs,oldWeight)+b)
            n = np.sum(np.dot(inputs,oldWeight))            
            a = hardLim(n)
            
            e = target - a
            if e == 1:
                newWeight = oldWeight + inputs
#                newB = oldB + e
                converge = False
                
            if e == -1:
                newWeight = oldWeight - inputs
#                newB = oldB - e
                converge = False
            
            oldWeight = newWeight

        #oldB =newB
    makePerceptronGraph(dataArr,newWeight)
    return newWeight

def makePerceptronGraph(dataArr,newWeight):
    gra.designFigure()
    gra.drawClassPoint(dataArr)  
    m,b = gra.getLineEquation(newWeight,[0,0])
    mPerpendicular = gra.getPerpendicularLineEquation(m)
#    drawEquationLine(m,b)
    gra.drawLine([newWeight],[0,0])
    gra.drawEquationLine(mPerpendicular,b)
    gra.drawPoints([newWeight], 'y*')
    gra.showGraph()
    

def hardLim(n):
#    print("n",n)
    if n >= 0:
        return 1
    else:
        return 0
    
perceptronTrainingAlgh(dataArr)

    
    
    



    
    
    
    
    
    
    
    