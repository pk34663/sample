import math

def calcradius(volume):
    v = volume*1e-09
    radius = (((volume*0.75)/(math.pi))**(1/3))

    return radius

def calcarea(volume,radius):
    v = volume*1e-09
    area = (4*math.pi*((radius)**(2)))

    return area
