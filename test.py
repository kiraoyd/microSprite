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
        turtle.moveTo(x, y)  
        sleep(rate)
    
    sleep(pause)
    
    for i in range(15):
        x = (x + 1) % 5
        turtle.moveTo(x, y)
        sleep(rate)
    
    sleep(pause)
    
    # Test Y Movement
    for i in range(15):
        y = (y + 1) % 5
        turtle.moveTo(x, y)
        sleep(rate)
    
    sleep(500)
    
    for i in range(15):
        y = (y - 1) % 5
        turtle.moveTo(x, y)
        sleep(rate)
    
    sleep(pause)

    #test the createCoordinatesForGroup function
    list = [4,4,4,3,4,2,4,1,4,0]
    coord = createCoordinatesForGroup(list)
    print (coord)
  
    wall = GroupOfSprites(list, brightness)
    wall.appear()
    sleep(pause)

    # Test Collision
    collision = False
    while collision == False:
        for cell in wall.sprites:
            
            if turtle.detectCollision(cell):
                display.show(Image.SAD)
                collision = True
                turtle.vanish()
                collision = True
                x = 2
                y = 2
                sleep(pause)

        if button_a.was_pressed():
            x = (x - 1) % 5
            turtle.moveTo(x, y)
            
        if button_b.was_pressed():
            x = (x + 1) % 5
            turtle.moveTo(x, y)


    print(id(wall))
    sleep(pause)

    ##### TEST GroupOfSprites #######

    #make group
    list = [{"x":2, "y":2}, {"x":2, "y":3}, {"x":2, "y":4}, {"x":1, "y":2}, {"x":1, "y":1}]
    group = GroupOfSprites(list, 9)
    group.appear()
    sleep(1000)
    group.moveLeftBy(1)
    sleep(1000)
    group.vanish()

    sleep(pause)

    # make wall, test takeDamage
    walllist = [{"x":2, "y":1}, {"x":2, "y":2}, {"x":2, "y":3}, {"x":2, "y":4}]
    wall = Wall(walllist, 9)
    wall.appear()
    sleep(1000)
    wall.vanish()
    wall.takeDamage([{"x":2, "y":2}], 4)
    wall.appear()
    sleep(1000)
    wall.vanish()

    sleep(pause)
    
    

