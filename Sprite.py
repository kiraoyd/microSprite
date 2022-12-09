# micro:sprite
# by Kira K & Mike W

#from microbit import *

def deleteSprite(Sprite):
    del Sprite


class Sprite:
    def __init__(self,startX, startY, brightness):
        self.__xCoord = startX
        self.__yCoord = startY
        self.__brightness = brightness

    def __del__(self):
        print("Sprite Destroyed!")

    def appear(self):
        display.set_pixel(self.__xCoord, self.__yCoord, self.__brightness) 

    def vanish(self):
        display.set_pixel(self.__xCoord, self.__yCoord, 0)
        
    def setBrightness(self, level):
        self.__brightness = level
        self.appear()
        
    def loseBrightness(self, level):
        self.__brightness = self.__brightness - level
        self.appear()

    def gainBrightness(self, level):
        self.__brightness = self.__brightness + level

    def moveTo(self, x,y):
        self.vanish()
        self.__xCoord = x
        self.__yCoord = y
        self.appear()
        return {"x":x, "y":y}

    def getPosition(self):
        return {"x":self.__xCoord, "y":self.__yCoord}

    def collisionDetected(self, obstacle):
      collide = False
      
      obstacle_position = obstacle.getPosition()
      
      if self.__xCoord == obstacle_position["x"] and self.__yCoord == obstacle_position["y"]:
        collide = True

      return collide