<<<<<<< HEAD
from exif import Image
from datetime import datetime
import math
from decimal import *
import time
#from picamera import PiCamera

#!MAXIM 5 CIFRE, DE CITIT DOCUMENTATIA

def decimal_coords(coords, ref):
    
    decimal_degrees = Decimal(coords[0] + coords[1] / 60 + coords[2] / 3600)
    if ref == "S" or ref =='W' :
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def image_coordinates(image_path):

    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
        except AttributeError:
            print ('No Coordinates')
    else:
        print ('The Image has no EXIF information')
        
    return(coords[0])

a=Decimal(6378.1370)
b=Decimal(6357.7523)
def earthRadius(lat):
    
    phi=Decimal(lat)
    cosine=Decimal(math.cos(phi))
    sine=Decimal(math.sin(phi))
    num=(((a*a)*cosine)**2+((b*b)*sine)**2)
    den=(Decimal(a*cosine)**2+Decimal(b*sine)**2)
    radius=Decimal(math.sqrt((num)/(den)))
    
    return radius


g=Decimal(6.673e-20)
m=Decimal(5.972e24)
def calcSpeed(radius, distance):
    
    r=radius+distance
    speed=Decimal(math.sqrt((g*m)/r))
    
    return speed

def takePicture(imgName):
    
    s=imgName
    return (calcSpeed(earthRadius(image_coordinates(s)), 403))

def getHeight():
    return 403

def calcImage(imgName):
    s='photo ('+ str(x)+').jpg'
    height = getHeight()
    calcSpeed(earthRadius(image_coordinates(s)), height)
 
 
def printOutput(speed):
    f = open("result.txt", "w") 
    rounded = "{:.4f}".format(speed)
    f.write(str(rounded))
    f.close()

def Program():
    mean = 0
    cnt = 0
    #cam = PiCamera()
    #cam.resolution = (1296, 972)
    
    for i in range(1,40):
        s='photo ('+ str(i)+').jpg'
        print(s)
        #fapoza()
        #cam.capture(fs)
        #calculeazadinpoza()
        mean += takePicture(s)
        cnt+=1
        #calcImage(s)
        time.sleep(1) #trebuie 15 ca sa avem 4 poze per minut, 1 e pentru testing, timpul e exprimat in secunde
    
    mean /= cnt
    printOutput(mean)
    
Program()
=======
from exif import Image
from datetime import datetime
import math
from decimal import *
from picamera import PiCamera

#!MAXIM 5 CIFRE, DE CITIT DOCUMENTATIA

def decimal_coords(coords, ref):
    
    decimal_degrees = Decimal(coords[0] + coords[1] / 60 + coords[2] / 3600)
    if ref == "S" or ref =='W' :
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def image_coordinates(image_path):

    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            img.gps_longitude
            coords = (decimal_coords(img.gps_latitude,
                      img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude,
                      img.gps_longitude_ref))
        except AttributeError:
            print ('No Coordinates')
    else:
        print ('The Image has no EXIF information')
        
    return(coords[0])

a=Decimal(6378.1370)
b=Decimal(6357.7523)
def earthRadius(lat):
    
    phi=Decimal(lat)
    cosine=Decimal(math.cos(phi))
    sine=Decimal(math.sin(phi))
    num=(((a*a)*cosine)**2+((b*b)*sine)**2)
    den=(Decimal(a*cosine)**2+Decimal(b*sine)**2)
    radius=Decimal(math.sqrt((num)/(den)))
    
    return radius


g=Decimal(6.673e-20)
m=Decimal(5.972e24)
def calcSpeed(radius, distance):
    
    r=radius+distance
    speed=Decimal(math.sqrt((g*m)/r))
    
    return speed

def takePicture():
    
    s=imgName
    print(calcSpeed(earthRadius(image_coordinates(s)), 403))

def getHeight():
    return 403

def calcImage(imgName):
    
    s='photo ('+ str(x)+').jpg'
    height = getHeight()
    calcSpeed(earthRadius(image_coordinates(s)), height)
 
 
def printOutput(speed):
    
    f = open("result.txt", "w") 
    rounded = "{:.4f}".format(speed)
    f.write(str(rounded))
    f.close()

def Program():
    cam = PiCamera()
    cam.resolution = (4056, 3040)
    for i in range(1,40):
        s='photo ('+ str(i)+').jpg'
        print(s)
        cam.capture(s)
        Sleep(400)
    #  fapoza()
    #  calculeazadinpoza()
        sleep(1e4)
    #
    #afiseaza()
>>>>>>> 2b20ec3e61e015d1d1d9e5c9b5e98caab2f0b763
