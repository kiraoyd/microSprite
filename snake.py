
from Sprite import *
from GroupOfSprites import *
from random import *
import math


startX = 0
startY = 4
snakeBrightness = 9

empty = []
snake = GroupOfSprites(empty, snakeBrightness)
snakeHead = Sprite(startX, startY, snakeBrightness)
snake.addSprite(snakeHead)
snake.appear()
score = 0

alive = True

while (alive):

    #generate an apple
    appleBrightness = 3
    appleX = math.floor(4*random())
    appleY = math.floor(4*random())
    apple = Sprite(appleX, appleY, appleBrightness)
    apple.appear()
    appleSpot = apple.getPosition()
    eaten = False

    while(not eaten):
    
        if accelerometer.was_gesture('up'):
            snake.moveUpBy(1)
        elif accelerometer.was_gesture('down'):
            snake.moveDownBy(1)
        elif accelerometer.was_gesture('left'):
            snake.moveLeftBy(1)
        elif accelerometer.was_gesture('right'):
            snake.moveRightBy(1)

        newSpritePositions = snake.getGroupPosition()

        
        if newSpritePositions[0]["x"] == appleSpot["x"] and newSpritePositions[0]["y"] == appleSpot["y"]:
            eaten = True
            apple.vanish()
            snake.appear()
            score += 1
            #how to grow the snake

        #the out of bounds check isn't working right....come back to this
        if newSpritePositions[0]["x"] > 4 or newSpritePositions[0]["x"] < 0:
            alive = False
            eaten = True
        
        if newSpritePositions[0]["y"] > 4 or newSpritePositions[0]["y"] < 0:
            alive = False
            eaten = True

display.scroll('apples: ', score)
display.show(Image.SKULL)
sleep(400)
            
