########################
##### flappy sprite ####
# running time version #
##### by Mike W ########
########################

# Import Starter Pack
from microbit import *
from microsprite import *
from groupofsprites import *
from random import randint, choice
import speech

# Clear Screen at Start
display.clear()

# Variable Starter Pack
you_lose = False
score = 0
x = 1
y = 2
brightness = 9

# Create Player
player = Sprite(x, y, brightness)


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

pipe_events = {'appear': 0,
               'move1': 0,
               'move2': 0,
               'move3': 0,
               'move4': 0,
               'move5': 0,
               'vanish': 0 }

pipe_intervals = {'appear': 1000,
                  'move1': 2000,
                  'move2': 3000,
                  'move3': 4000,
                  'move4': 5000,
                  'move5': 6000,
                  'vanish': 7000 }

while True:
    current_time = running_time()
    x = 4
    pipe = choice(pipes)
    
    if current_time - pipe_events['appear'] >= pipe_intervals['appear']:
        pipe.appear()
        pipe_events['appear'] = running_time()
    
    if current_time - pipe_events['move1'] >= pipe_intervals['move1']:     
        pipe.moveToX(3)
        x -= 1
        pipe_events['move1'] = running_time()

    if current_time - pipe_events['move2'] >= pipe_intervals['move2']:     
        pipe.moveToX(2)
        x -= 1
        pipe_events['move2'] = running_time()

    if current_time - pipe_events['move3'] >= pipe_intervals['move3']:     
        pipe.moveToX(1)
        x -= 1
        pipe_events['move3'] = running_time()

    if current_time - pipe_events['move4'] >= pipe_intervals['move4']:     
        pipe.moveToX(0)
        x -= 1
        pipe_events['move4'] = running_time()
    
    
    if current_time - pipe_events['vanish'] >= pipe_intervals['vanish']:
        pipe.vanish()
        pipe_events['vanish'] = running_time()
    
    
        
    
    
