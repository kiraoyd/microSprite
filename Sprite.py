# micro:sprite
# by Kira K & Mike W

#from microbit import *

def deleteSprite(Sprite):
    del Sprite

class Location(object):

    def __init__(self, startX, startY):
        self.__xCoord = startX
        self.__yCoord = startY


    def collisionDetected(self, x, y):
        collide = False
        if self.__xCoord == x and self.yCoord == y:
            brightness = display.get_pixel(x,y)
            if(brightness > 0):
                collide = True
        return collide


class Sprite(Location):
    """Implements methods to manipulate a single LED at some location (x,y) on the Micro:bit display"""
    
    def __init__(self,startX, startY, brightness):
        Location.__init__(self, startX, startY)
        self.__brightness = brightness

    def __del__(self):
        print("Sprite Destroyed!")

    def appear(self):
        """Turns 'on' this Sprite by activating the LED with its specified brightness"""

        display.set_pixel(self.__xCoord, self.__yCoord, self.__brightness) 

    def vanish(self):
        """Turns 'off' this Sprite by activating the LED at a brightness level of 0 (none)"""

        display.set_pixel(self.__xCoord, self.__yCoord, 0)
        
    def setBrightness(self, level):
        """Sets the brightness level for this Sprite to a value between 0 (no brightness) and 9 (highest brightness), specified by the argument"""

        self.__brightness = level
        self.appear()
        
    def loseBrightness(self, level):
        """Reduces the brightness for this Sprite by a specified amount"""

        self.__brightness = self.__brightness - level
        self.appear()

    def gainBrightness(self, level):
        """Increases the brightness for this Sprite by a specified amount"""

        self.__brightness = self.__brightness + level

    def moveTo(self, x,y):
        """Turns off the LED, resets the Sprite to a new (x,y) location, and turns on the LED found at the new (x,y) location. """

        self.vanish()
        self.__xCoord = x
        self.__yCoord = y
        self.appear()

    def getPosition(self):
        """Returns, as a dictionary, the (x,y) position this Sprite occupies when called"""

        return {"x":self.__xCoord, "y":self.__yCoord}

    def collisionWithSpriteDetected(self, obstacle):
        """Takes in another Sprite as an argument, and returns True if that Sprite is in the same position as this Sprite"""
        
        collide = False

        obstacle_position = obstacle.getPosition()

        if self.__xCoord == obstacle_position["x"] and self.__yCoord == obstacle_position["y"]:
            collide = True
            
        return collide
            