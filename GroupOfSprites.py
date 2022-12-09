from Sprite import *
from time import sleep


def createCoordinatesForGroup(list):
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
    def __init__(self, listOfCoordinates, brightness):
        self.__numberOfSprites = len(listOfCoordinates)
        self.__coordinates = listOfCoordinates
        self.__sprites = []
        self.__brightness = brightness
      
        #instantiate Sprites
        for sprite in listOfCoordinates:
            self.__sprites.append(Sprite(sprite["x"], sprite["y"], self.__brightness))
            print("Sprite added") #testline

    def addSprite(self, sprite):
        self.__sprites.append(sprite)


    def getGroupPosition(self):
        """Returns a list of {"x":x, "y":y} coordinate dictionaries, representing the current locations of all Sprites in this Group"""

        spriteLocations = []
        for sprite in self.__sprites:
            position = sprite.getPosition()
            spriteLocations.append(position)
        return spriteLocations
            
    def appear(self):
        for sprite in self.__sprites:
            sprite.appear()

    def vanish(self):
        for sprite in self.__sprites:
            sprite.vanish()

    def setBrightness(self, brightness):
        for sprite in self.__sprites:
            sprite.setBrightness(brightness)

    #check for out of bounds needs to be handled by each Sprites moveTo() call
    def moveLeftBy(self, moves):
        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] - moves
            return sprite.moveTo(position["x"], position["y"])
           


    def moveRightBy(self, moves):
        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] + moves
            return sprite.moveTo(position["x"], position["y"])
            

    def moveUpBy(self, moves):
        for sprite in self.__sprites:
            position = sprite.getPosition()
            position["y"] = position["y"] - moves
            return sprite.moveTo(position["x"], position["y"])
  

    def moveDownBy(self,moves):
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
    def __init__(self, listOfCoordinates, brightness):
        GroupOfSprites.__init__(self, listOfCoordinates, brightness)

    def takeDamage(self, coordinatesHit, brightnessLost):
        for sprite in self.__sprites:
            position = sprite.getPosition()
            index = 0
            while(index < len(coordinatesHit)):
                if(coordinatesHit[index]["x"] == position["x"] and coordinatesHit[index]["y"] == position["y"]):
                    sprite.loseBrightness(brightnessLost)
                index += 1
