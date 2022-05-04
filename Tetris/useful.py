from math import sqrt
import euclid
'''
A library i created that has generally useful functions, so far they're just vector math functions
'''

#the function i most commonly use, this is used to calculate the new magnitude of a vector, vector is the Vector2 object that you wish to have the magnitude set
#DesiredMag is the magnitude value that you want
def setMag(vector, desiredMag):
    
    #just checks if the squared value of the vector is zero since it will throw up an error if it is
    if vector.magnitude_squared():
        #Calculates the new vector using a formula i pulled off the internet
        newVector = vector * desiredMag / vector.magnitude_squared()
    else:
        #if it does equal to zero or an otherwise non true value, then just leave it out, or effectivly set it to 1
        newVector = vector * desiredMag
    
    #return it once done!!
    return newVector

#Used to find the distance between two vectors (points on a graph). You have most commonly used the equation in Algebra 2 and Geometry
def findDist(vector1, vector2):
    d = 0 
    #Distance equation
    d = sqrt((vector2.x - vector1.x) * (vector2.x - vector1.x)) + ((vector2.y - vector1.y) * (vector2.y - vector1.y))
    #return it once done!!
    return d

def findSlope(vector1, vector2):
    newVector = euclid.Vector2(vector2.x - vector1.x, vector2.y - vector1.y)
    return newVector

def create2DArray(x, y, value):
    array = []
    for i in range(y):
        array.append([])
        for j in range(x):
            array[i].append(value)
    
    return array