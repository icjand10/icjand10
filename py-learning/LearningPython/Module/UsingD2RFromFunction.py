import math
def degreestoradian(x):
    pi = math.pi
    radian = x * pi/180
    return radian
print(degreestoradian(6))

def radiantodegrees(y):
    pi = math.pi
    degrees = y * 180/pi
    return degrees
print(radiantodegrees(6))
