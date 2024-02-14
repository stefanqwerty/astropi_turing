from exif import Image
from datetime import datetime
import math
from decimal import *

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

#print(image_coordinates('photo_0683.jpg'))

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

for x in range(1, 55):
    s='photo ('+ str(x)+').jpg'
    print(calcSpeed(earthRadius(image_coordinates(s)), 403))
    
