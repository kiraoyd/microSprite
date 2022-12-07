'''
#################################
### micro:sprite - Test Suite ###
##### by Kira K & Mike W ########
#################################

A series of tests of our micro:sprite library
'''

from microbit import *
import microsprite
from random import randint


# Starting Coordinates
x = 2
y = 2

# Brightness
brightness = 9

# Start the Sprite
turtle = microsprite.Sprite(x, y, brightness)
turtle.on()

# Show Off Attributes

# Test Brightness
for i in range(5):
    for i in range(9, 0, -1):
        turtle.setBrightness(i)
        sleep(50)  
    for i in range(9):
        turtle.setBrightness(i)
        sleep(50)
      
sleep(500)

# Test X Movement
for i in range(15):
    x = (x - 1) % 5
    turtle.off()
    turtle.moveTo(x, y)
    turtle.on()    
    sleep(250)

sleep(500)

for i in range(15):
    x = (x + 1) % 5
    turtle.off()
    turtle.moveTo(x, y)
    turtle.on()
    sleep(250)

sleep(500)

# Test Y Movement
for i in range(15):
    y = (y + 1) % 5
    turtle.off()
    turtle.moveTo(x, y)
    turtle.on()
    sleep(250)

sleep(500)

for i in range(15):
    y = (y - 1) % 5
    turtle.off()
    turtle.moveTo(x, y)
    turtle.on()
    sleep(250)

sleep(500)

    

