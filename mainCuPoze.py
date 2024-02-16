from exif import Image
from math import *
from decimal import Decimal
from time import sleep
from datetime import datetime
from picamera import PiCamera
from orbit import ISS

def decimalCoords(coords, ref):
    
    decDegrees = Decimal(coords[0] + coords[1] / 60 + coords[2] / 3600)
    if ref == "S" or ref =='W' :
        decDegrees = -decDegrees
    return decDegrees

def image_coordinates(imgName):

    with open(imgName, 'rb') as source:
        img = Image(source)
    if img.has_exif:
        try:
            coords = (decimalCoords(img.gps_latitude,img.gps_latitude_ref),
					  decimalCoords(img.gps_longitude,img.gps_longitude_ref))
        except AttributeError:
            print ('no coordinates')
    else:
        print ('no EXIF information')
        
    return(coords[0])

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

def getHeight():
    
    location = ISS().coordinates()
    height = Decimal(location.elevation.km)
    return height

def calcImage(imgName):
    
    s = imgName
    return (calcSpeed(earthRadius(image_coordinates(s)), getHeight()))
 
def printOutput(speed):
    
    f = open("result.txt", "w", encoding="ascii") 
    formatted = "{:.4f}".format(speed)
    f.write(str(formatted))
    f.close()

def Program():
    
    mean = Decimal(0)
    cnt = 0
    cam = PiCamera()
    cam.resolution = (4056, 3040)
    picNumber = 5
    mins = 1
    secs = 0
    time = mins * 60 + secs
    startTime = datetime.now()
    
    for i in range(1, picNumber+1):
        currentTime = datetime.now()
        print(f'au trecut {(currentTime-startTime).seconds} secunde')
        if((currentTime-startTime).seconds >= time):
            break
        s = f'photo({i}).jpg'
        cam.capture(s)
        print(f'facut poza {s}')
        mean += calcImage(s)
        cnt += 1
        print(f'average: {mean/cnt}')
    
    mean /= cnt
    printOutput(mean)
    
Program()