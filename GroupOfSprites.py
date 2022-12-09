from Sprite import *
from time import sleep


def createCoordinatesForGroup(list):
    """Takes a list of numbers representing repeating x and y values, and transforms them into a list of (x,y) dictionaries. Each dictionary has the key value pairng: {"x":x, "y":y}"""
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
    """A collection of single sprites represented by a collection of (x,y) locations for LED's on the Micro:bit display"""

    def __init__(self, listOfCoordinates, brightness):
        self.__numberOfSprites = len(listOfCoordinates)
        self.__sprites = []
        self.__brightness = brightness
      
        #instantiate Sprites
        for location in listOfCoordinates:
            self.sprites.append(Sprite(location["x"], location["y"], self.brightness))
            print("Sprite added") #testline

    def getGroupPosition(self):
        """Returns a list of {"x":x, "y":y} coordinate dictionaries, representing the current locations of all Sprites in this Group"""

        spriteLocations = []
        for sprite in self.__sprites:
            position = sprite.getPosition()
            spriteLocations.append(position)
        return spriteLocations
            
    def appear(self):
        """Turns 'on' this group of Sprites by activating the LED for each sprite at its specified brightness"""

        for sprite in self.__sprites:
            sprite.appear()

    def vanish(self):
        """Turns 'off' this group of Sprites by activating the LED for each sprite at a brightness level of 0 (none)"""

        for sprite in self.__sprites:
            sprite.vanish()

    def setBrightness(self, brightness):
        """Sets the brightness level for this group of Sprites to a value between 0 (no brightness) and 9 (highest brightness), specified by the argument"""

        for sprite in self.__sprites:
            sprite.setBrightness(brightness)

    #check for out of bounds needs to be handled by each Sprites moveTo() call
    def moveLeftBy(self, moves):
        """Moves the entire group of Sprites to the left by the number of moves specified by the argument"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] - moves
            return sprite.moveTo(position["x"], position["y"])
           


    def moveRightBy(self, moves):
        """Moves the entire group of Sprites to the right by the number of moves specified by the argument"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] + moves
            return sprite.moveTo(position["x"], position["y"])
            

    def moveUpBy(self, moves):
        """Moves the entire group of Sprites to the up by the number of moves specified by the argument"""

        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["y"] = position["y"] - moves
            return sprite.moveTo(position["x"], position["y"])
  

    def moveDownBy(self,moves):
        """Moves the entire group of Sprites down by the number of moves specified by the argument"""

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
    """A group of Sprites with specific functionality to have it behave as a Wall obstacle"""

    def __init__(self, listOfCoordinates, brightness):
        GroupOfSprites.__init__(self, listOfCoordinates, brightness)

    def takeDamage(self, coordinatesHit, brightnessLost):
        """Reduces the brightness level by the arguments specified 'brightnesLost' amount, for the Sprites LED location(s) specified by the 'coordinatesHit' argument  """

        for sprite in self.sprites:
            position = sprite.getPosition()
            index = 0
            while(index < len(coordinatesHit)):
                if(coordinatesHit[index]["x"] == position["x"] and coordinatesHit[index]["y"] == position["y"]):
                    sprite.loseBrightness(brightnessLost)
                index += 1


