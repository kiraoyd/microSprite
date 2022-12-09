from Sprite import *
from GroupOfSprites import *
from random import *
import math


startX = 0
startY = 4
snakeBrightness = 5

empty = []
snake = GroupOfSprites(empty, snakeBrightness)
snakeHead = Sprite(startX, startY, snakeBrightness)
snake.addSprite(snakeHead)

alive = true

while (alive):

    #generate an apple
    appleBrightness = 5
    appleX = math.floor(4*random())
    appleY = math.floor(4*random())
    apple = Sprite(appleX, appleY, appleBrightness)
    apple.appear()
    appleSpot = apple.getPosition()
    eaten = False

    while(not eaten):
        position = {}
        if accelerometer.was_gesture('up'):
            position = snake.moveUpBy(1)
        elif accelerometer.was_gesture('down'):
            position = snake.moveDownBy(1)
        elif accelerometer.was_gesture('left'):
            position = snake.moveLeftBy(1)
        elif accelerometer.was_gesture('right'):
            position = snake.moveRightBy(1)

        
        if position["x"] == appleSpot["x"] and position["y"] == appleSpot["y"]:
            eaten = True
            apple.vanish()
            #how to grow the snake

        if position["x"] > 4:
            

            

    

