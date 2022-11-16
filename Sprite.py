
import abc
from abc import ABC
#How do we get the microbit code imported?

class Sprite:
    def __init__(self):
        self.xCoord = 0
        self.yCoord = 0
        self.brightness = 0

    def createSprite(self, startX, startY, brightness):
        self.xCoord = startX
        self.yCoord = startY
        self.brightness = brightness
        display.set_pixel() #need to connect to microbit code

    def setBrightness(self, level):
        self.brightness = level
        


class Obstacle(ABC):
    def __init__(self):
        self.ledsOn = []
        self.brightness = 0

class Wall(Obstacle):
    def __init__(self):
        pass


class MovingPipes(Obstacle):
    def __init__(self):
        pass

