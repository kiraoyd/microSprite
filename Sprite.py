# micro:sprite
# by Kira K & Mike W

from microbit import *

def deleteSprite(Sprite):
    del Sprite

class Location(object):
    """Base class, implements methods for a single (x,y) location on the Micro:bit LED display."""

    def __init__(self, startX, startY):
        self.__xCoord = startX
        self.__yCoord = startY


    def collisionDetected(self, x, y):
        """Takes in a value for an x-coordinate and a value for a y-coordinate, if they match this Sprites coordinates and the LED has a brightness > 0, this function returns True, otherwise returns False"""

        collide = False
        if self.__xCoord == x and self.__yCoord == y:
            brightness = display.get_pixel(x,y)
            if(brightness > 0):
                collide = True
        return collide


class Sprite(Location):
    """Extends the Location class, implements methods to manipulate a Sprite (represented by a single LED) at some location (x,y) on the Micro:bit display"""
    
    def __init__(self,startX, startY, brightness):
        Location.__init__(self, startX, startY)
        self.__brightness = brightness

    def __del__(self):
        print("Sprite Destroyed!")

    def inBounds(self):
        """Returns True if the Sprites x and y coordinates are in bounds of the 5x5 Micro:bit display. The LED at the upper left corner of the display represents coordinate (0,0)"""
        inBound = False
        if(self.__xCoord <= 4 and self.__xCoord >= 0):
            if(self.__yCoord <=4 and self.__yCoord >= 0):
                inBound = True
        return inBound

    def appear(self):
        """Turns 'on' this Sprite by activating the LED with its specified brightness"""
        if self.inBounds():
            display.set_pixel(self.__xCoord, self.__yCoord, self.__brightness) 
        else:
            print("Sorry that locaton is out of display bounds, we cannot show it")
        
    def vanish(self):
        """Turns 'off' this Sprite by activating the LED at a brightness level of 0 (none)"""
        if self.inBounds():
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
        """Turns off the LED, resets the Sprite to a new (x,y) location, turns on the LED found at the new (x,y) location, and returns the coordinates of the new location in the form: {"x":xVal, "y":yVal}"""
        self.vanish()
        self.__xCoord = x
        self.__yCoord = y
        self.appear()
        return {"x":x, "y":y}

    def getPosition(self):
        """Returns the (x,y) position this Sprite occupies, in the form: {"x":xVal, "y":yVal}"""

        return {"x":self.__xCoord, "y":self.__yCoord}

    def collisionWithSpriteDetected(self, obstacle):
        """Takes in another Sprite as an argument, and returns True if that Sprite is in the same (x,y) position as this Sprite"""
        
        collide = False
        obstacle_position = obstacle.getPosition()
        if self.__xCoord == obstacle_position["x"] and self.__yCoord == obstacle_position["y"]:
            collide = True
        return collide
            