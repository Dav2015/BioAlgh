

import matplotlib.pyplot as plt
import numpy as np

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
        print([point])
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