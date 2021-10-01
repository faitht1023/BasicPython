'''
Circle Problem Solution
Sonia Wong
'''

from sympy import *

#Takes user input for points on the line
linePointA = input("Coordinate(x1,y1): ").split()
linePointA = [int(i) for i in linePointA]
linePointB = input("Coordinate(x2,y2): ").split()
linePointB = [int(i) for i in linePointB]
print(linePointA, linePointB)

#Takes user input for Circle data
centerPoint = input("Circle Coordinate(x,y)").split()
