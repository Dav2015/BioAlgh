# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random as rnd
import numpy as np
import matplotlib.pyplot as plt

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
    designFigure()
    drawClassPoint(dataArr)  
    m,b = getLineEquation(newWeight,[0,0])
    mPerpendicular = getPerpendicularLineEquation(m)
#    drawEquationLine(m,b)
    drawLine([newWeight],[0,0])
    drawEquationLine(mPerpendicular,b)
    drawPoints([newWeight], 'y*')
    showGraph()
    

def hardLim(n):
#    print("n",n)
    if n >= 0:
        return 1
    else:
        return 0
    
def drawPoints(points,color):
    for point in points:
        plt.plot(point[0],point[1],color)
        
def drawClassPoint(points):
    classColors = {
		0 : 'bo',
		1 : 'go',
		2 : 'ko',
		3:'mo'
	}
    for point in points:
#        print([point])
        drawPoints([point],classColors[point[2]])
            
def drawLine(point1,point2):
    xy = np.vstack((point1,point2)).transpose()
    plt.plot(xy[0],xy[1],'ko-')
        
def showGraph():
    plt.show()
    
def designFigure():
    plt.figure()
    plt.xlim([-4,4])
    plt.ylim([-4,4])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    

def getLineEquation(point1,point2):
    x1 = point1[0]
    y1 = point1[1]
    
    x2 = point2[0]
    y2 = point2[1]
    
    m = (y2-y1)/(x2-x1)
    b = -m*x1+y1
    return m,b
    

def getPerpendicularLineEquation(m):
    mPerpendicular = m/-(m*m)
    return mPerpendicular


def drawEquationLine(m,b):
    x = np.linspace(-15,15,10) # 100 linearly spaced numbers
    
    y = np.zeros((1,len(x))).ravel()
    for i in range(len(x)):    
        y[i] = m*x[i] + b
    
    plt.plot(x,y)
    return x,y

perceptronTrainingAlgh(dataArr)

    
    
    



    
    
    
    
    
    
    
    