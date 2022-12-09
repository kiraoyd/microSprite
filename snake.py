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
    eaten = False

    while(not eaten):
        if accelerometer.was_gesture('up'):
            snake.moveUpBy(1)
        elif accelerometer.was_gesture('down'):
            snake.moveDownBy(1)
        elif accelerometer.was_gesture('right'):
            snake.moveRightBy(1)
        elif accelerometer.was_gesture('left'):
            snake.moveLeftBy(1)

        if


    

