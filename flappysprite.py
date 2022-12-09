#####################
### flappy sprite ###
##### by Mike W #####
#####################

from microbit import *
from Sprite import *
from GroupOfSprites import *
from random import randint, choice

display.clear()

x = 1
y = 2
brightness = 9

player = Sprite(x, y, brightness)
player.appear()

pipe_x = 4
pipe0 = GroupOfSprites([{"x": pipe_x, "y": 4}, {"x": pipe_x, "y": 3}], 9)
pipes = [pipe0]

while True:
    pipe_boundary = 5
    pipe = choice(pipes)
    
    while pipe_boundary > 1:
        # Create Wall
        pipe.appear()
        
        # Move Wall
        pipe_boundary -= 1
        pipe.moveLeftBy(1)
        sleep(0.24)
        
        
        # Player Fall Down
        if y >= 4:
            y = 4
        else:
            y = y + 1
            
        player.moveTo(x,y)
        sleep(0.75)
    
    
        # Player Flap
        if button_a.was_pressed():
            # Player Boundary
            if y <= 1:
                y = 0
            else:
                y = y - 2
                
            player.moveTo(x,y)
            sleep(0.5)

    pipe.vanish()
        
    

