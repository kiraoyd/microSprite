#####################
### flappy sprite ###
##### by Mike W #####
#####################

from microbit import *
from Sprite import *
from GroupOfSprites import *
from random import randint, choice

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

while not you_lose:
    pipe_boundary = 5
    pipe = choice(pipes)
    pipe_x_coord = 4
    
    while pipe_x_coord >= 0:
        # Create Wall
        pipe.appear()
        sleep(250)
        
        # Move Wall
        pipe.moveToX(pipe_x_coord)
        pipe_x_coord = pipe_x_coord - 1
        sleep(250)
  
        # Detect Collision
        pipe_coordinates = pipe.getGroupPosition()
        player_position = player.getPosition()
    
        
        if player_position in pipe_coordinates:
            player.vanish()
            sleep(100)
            pipe.vanish()
            sleep(100)
            display.clear()
            audio.play(Sound.SAD)
            display.show(Image.ANGRY)
            display.scroll("SCORE: " + str(score))
            sleep(500)
            display.scroll("GAME OVER")
            sleep(250)
            
            pipe_x_coord = -999
            you_lose = True
            
        # Player Flap
        if button_a.was_pressed():
            # Player Boundary
            if y <= 1:
                y = 0
            else:
                y = y - 1
                    
        else:
            # Player Fall Down
            if y >= 4:
                y = 4
            else:
                y = y + 1
        player.moveTo(x,y)
        sleep(250)

    else:
        score += 1

    pipe.vanish()

display.clear()
reset()
    

