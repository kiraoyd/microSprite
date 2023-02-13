#####################
### flappy sprite ###
##### by Mike W #####
#####################

# Import Starter Pack
from microbit import *
from microsprite import *
from groupofsprites import *
from random import randint, choice
import speech

# Clear Screen at Start
display.clear()

# Variable Starter Pack
x = 1
y = 0
brightness = 9
score = 0

# Create Player
player = Sprite(x, y, brightness)
player.appear()

# Create the Obstacles
pipe0 = GroupOfSprites([
                        {'x': 4, 'y': 4}, 
                        {'x': 4, 'y': 3},], 
                        brightness)
pipe1 = GroupOfSprites([
                        {'x': 4, 'y': 4}, 
                        {'x': 4, 'y': 3}, 
                        {'x': 4, 'y': 2}],
                        brightness)
pipe2 = GroupOfSprites([
                        {'x': 4, 'y': 4}, 
                        {'x': 4, 'y': 3}, 
                        {'x': 4, 'y': 2},
                        {'x': 4, 'y': 1}],
                        brightness)
pipe3 =  GroupOfSprites([
                        {'x': 4, 'y': 4}, 
                        {'x': 4, 'y': 3},
                        {'x': 4, 'y': 0}], 
                        brightness)
pipes = [pipe0, pipe1, pipe2, pipe3]

# timing variables
PIPE_DELAY = 800
FALL_DELAY = 1000
FLAP_DELAY = 200

flap_time1 = 0
flap_time2 = 0
pipe_time = 0
fall_time = 0
stall_time = 0

# Create a Pipe
pipe = choice(pipes)
pipe.appear()
x = 4


while True:

    # Capture Time
    elapsed_time_flap1 = running_time()
    elapsed_time_flap2 = running_time()
    elapsed_time_pipe = running_time()
    elapsed_time_fall = running_time()
    elapsed_time_stall = running_time()

    # Flap
    if button_a.was_pressed():
        y = y - 1
        if y < 0:
            y = 0
            
        
        player.moveTo(1, y)
        flap_time1 = running_time()
    
    
    # Collision
    elif player.getPosition() in pipe.getGroupPosition():
        print('crash')
        break
            
    # Fall
    elif elapsed_time_fall - fall_time >= FALL_DELAY:
        y = y + 1
        if y > 4:
            y = 4

        player.moveTo(1, y)
        fall_time = running_time()

    elif elapsed_time_stall - stall_time >= 2000:
        player.moveTo(1, y)
        stall_time = running_time()
            
    # Wall
    elif elapsed_time_pipe - pipe_time >= PIPE_DELAY:
        x -= 1
        if x <= -1:
            x = 4
            score += 1
            pipe.vanish()
            pipe = choice(pipes)
            pipe.appear()
            
        else:
            pipe.moveToX(x)
        
        pipe_time = running_time()

display.show(Image.SKULL)
sleep(500)
display.scroll(score)