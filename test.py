'''
#################################
### micro:sprite - Test Suite ###
##### by Kira K & Mike W ########
#################################

A series of tests of our micro:sprite library
'''

from microbit import *
from Sprite import *
from GroupOfSprites import *
from random import randint

display.clear()

# Starting Values
x = 2
y = 2
brightness = 9
rate = 50
speed = 50
pause = 500
long_pause = 3000


while True:
    # Start the Sprite
    turtle = Sprite(x, y, brightness)
    turtle.appear()
    
    
    # Clear Screen
    display.clear()
    
    # Test Brightness
    for i in range(5):
        for i in range(9, 0, -1):
            turtle.setBrightness(i)
            sleep(rate)  
        for i in range(9):
            turtle.setBrightness(i)
            sleep(rate)
          
    sleep(pause)

    # Test X Movement
    for i in range(15):
        x = (x - 1) % 5
        turtle.vanish()
        turtle.moveTo(x, y)
        turtle.appear()    
        sleep(rate)
    
    sleep(pause)
    
    for i in range(15):
        x = (x + 1) % 5
        turtle.vanish()
        turtle.moveTo(x, y)
        turtle.appear()
        sleep(rate)
    
    sleep(pause)
    
    # Test Y Movement
    for i in range(15):
        y = (y + 1) % 5
        turtle.vanish()
        turtle.moveTo(x, y)
        turtle.appear()
        sleep(rate)
    
    sleep(500)
    
    for i in range(15):
        y = (y - 1) % 5
        turtle.vanish()
        turtle.moveTo(x, y)
        turtle.appear()
        sleep(rate)
    
    sleep(pause)

    list = [{"x": 4, "y": 4}, 
            {"x": 4, "y": 3}, 
            {"x": 4, "y": 2}, 
            {"x": 4, "y": 1},
            {"x": 4, "y": 0}]
    
    wall = GroupOfSprites(list, brightness)
    wall.appear()
    sleep(pause)

    # Test Collision
    collision = False
    while collision == False:
        for cell in wall.sprites:
            
            if turtle.collision(cell):
                sleep(pause)
                display.show(Image.SAD)
                collision = True
                turtle.vanish()
                collision = True
                x = 2
                y = 2
                sleep(pause)

        if button_a.was_pressed():
            x = (x - 1) % 5
            turtle.vanish()
            turtle.moveTo(x, y)
            turtle.appear()
            
        if button_b.was_pressed():
            x = (x + 1) % 5
            turtle.vanish()
            turtle.moveTo(x, y)
            turtle.appear()

    print(id(wall))
    sleep(pause)
    
    

