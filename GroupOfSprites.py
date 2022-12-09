from Sprite import *
from time import sleep


def createCoordinatesForGroup(list):
    """Takes in a list of numbers representing repeating x and y values, and stores them in a list them into the form: {"x":xVal, "y":yVal}"""

    xIndex = 0
    yIndex = 1
    coordinates = []
    while yIndex < len(list):
        temp = {"x":0, "y":0}
        temp["x"] = list[xIndex]
        temp["y"] = list[yIndex]
        coordinates.append(temp)
        xIndex += 1
        yIndex += 1
    return coordinates


class GroupOfSprites(object):
    """Base class, implements methods for manipulating a collection of single Sprites at locations specified by the listOfCoordinates argument, at a level of brightness specified by the brightness argument, on the Micro:bit display"""

    def __init__(self, listOfCoordinates, brightness):
        self.__numberOfSprites = len(listOfCoordinates)
        self.__coordinates = listOfCoordinates
        self.__sprites = []
        self.__brightness = brightness
      
        #instantiate Sprites
        for sprite in listOfCoordinates:
            self.__sprites.append(Sprite(sprite["x"], sprite["y"], self.__brightness))


    def addSprite(self, sprite):
        """Appends a new sprite to the list of sprites for this group"""

        self.__sprites.append(sprite)


    def getGroupPosition(self):
        """Returns a list of {"x":x, "y":y} coordinate dictionaries, representing the current locations of all Sprites in this Group"""

        spriteLocations = []
        for sprite in self.__sprites:
            position = sprite.getPosition()
            spriteLocations.append(position)
        return spriteLocations
            
    def appear(self):
        """Turns on each Sprite in this GroupOfSprites"""

        for sprite in self.__sprites:
            sprite.appear()

    def vanish(self):
        """Turns off each Sprite in this GroupOfSprites"""

        for sprite in self.__sprites:
            sprite.vanish()

    def setBrightness(self, brightness):
        """Sets the brightness for each Sprite in thie GroupOfSprites to a brightness specified by the argument"""

        for sprite in self.__sprites:
            sprite.setBrightness(brightness)

    def moveLeftBy(self, moves):
        """Shifts each Sprite in this GroupOfSprites to the left along the x-axis by 'moves' number of LEDs"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] - moves
            return sprite.moveTo(position["x"], position["y"])
           

    def moveRightBy(self, moves):
        """Shifts each Sprite in this GroupOfSprites to the right along the x-axis by 'moves' number of LEDs"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] + moves
            return sprite.moveTo(position["x"], position["y"])
            

    def moveUpBy(self, moves):
        """Shifts each Sprite in this GroupOfSprites up along the y-axis by 'moves' number of LEDs"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["y"] = position["y"] - moves
            return sprite.moveTo(position["x"], position["y"])
  

    def moveDownBy(self,moves):
        """Shifts each Sprite in this GroupOfSprites down along the y-axis by 'moves' number of LEDs"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["y"] = position["y"] + moves
            return sprite.moveTo(position["x"], position["y"])


    #Another option for how to move
    def moveToX(self, newX):
        """Moves the entire group of Sprites along the x-axis, to the x-axis value specified by the argument. A move to the left should take a negative number as an argument, and a move to the right a positive number"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            sprite.moveTo(newX, position["y"])

    def moveToY(self, newY):
        """Moves the entire group of Sprites along the y-axis, to the y-axis value specified by the argument. A move up should take a negative number as an argument, and a move down a positive number"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            sprite.moveTo(position["x"], newY)


class Wall(GroupOfSprites):
    """Extends GroupOfSprites, implements the methods for a specific GroupOfSprites to act as a Wall"""

    def __init__(self, listOfCoordinates, brightness):
        GroupOfSprites.__init__(self, listOfCoordinates, brightness)

    def takeDamage(self, coordinatesHit, brightnessLost):
        """Reduces the brightness of the LED Sprite's found at each location in the coordinatesHit argument, by the specified brightnessLost level argument"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            index = 0
            while(index < len(coordinatesHit)):
                if(coordinatesHit[index]["x"] == position["x"] and coordinatesHit[index]["y"] == position["y"]):
                    sprite.loseBrightness(brightnessLost)
                index += 1
