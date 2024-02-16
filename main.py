from math import *
from decimal import Decimal
from time import sleep
from datetime import datetime
from orbit import ISS

a = Decimal(6378.1370)
b = Decimal(6357.7523)
def earthRadius(latitude):
    
    phi = Decimal(latitude)
    cosine = Decimal(cos(phi))
    sine = Decimal(sin(phi))
    
    num = (((a * a) * cosine)**2 + ((b * b) * sine)**2)
    den=(Decimal(a * cosine)**2 + Decimal(b * sine)**2)
    radius=Decimal(sqrt((num) / (den)))
    
    return radius

g = Decimal(6.673e-20)
m = Decimal(5.972e24)
def calcSpeed(radius, distance):
    
    r = radius + distance
    speed = Decimal(sqrt((g * m) / r))
    return speed

def calcFromLocation():
    
    location = ISS().coordinates()
    
    latitude = Decimal(location.latitude.degrees)
    height = Decimal(location.elevation.km)
    
    #print(f'latitude: {latitude}')
    #print(f'height: {height}')
    
    return (calcSpeed(earthRadius(latitude), height))
 
def printOutput(speed):
    
    f = open("result.txt", "w", encoding="ascii")
    
    formatted = "{:.4f}".format(speed)
    f.write(str(formatted))
    
    f.close()

def Program():
    
    mean = Decimal(0)
    cnt = 0
    iterations = 50
    
    mins = 9
    secs = 30
    time = mins * 60 + secs
    
    startTime = datetime.now()
    
    for i in range(1, iterations+1):
        
        currentTime = datetime.now()
        if((currentTime-startTime).seconds >= time):
            break
        #print(f'au trecut {(currentTime-startTime).seconds} secunde')
        
        mean += calcFromLocation()
        cnt += 1
        #print(f'average: {mean/cnt}')
        
        sleep(15)
    
    mean /= cnt
    printOutput(mean)
    
Program()