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
        self.numberOfSprites = len(listOfCoordinates)
        self.coordinates = listOfCoordinates
        self.sprites = []
        self.brightness = brightness
      
        #instantiate Sprites
        for sprite in listOfCoordinates:
            self.sprites.append(Sprite(sprite["x"], sprite["y"], self.brightness))
            print("Sprite added") #testline

    def appear(self):
        for sprite in self.sprites:
            sprite.appear()

    def vanish(self):
        for sprite in self.sprites:
            sprite.vanish()

    def setBrightness(self, brightness):
        for sprite in self.sprites:
            sprite.setBrightness(brightness)

    #check for out of bounds needs to be handled by each Sprites moveTo() call
    def moveLeftBy(self, moves):
        for sprite in self.sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] - moves
            sprite.moveTo(position["x"], position["y"])


    def moveRightBy(self, moves):
        for sprite in self.sprites:
            position = sprite.getPosition()
            position["x"] = position["x"] + moves
            sprite.moveTo(position["x"], position["y"])

    def moveUpBy(self, moves):
        for sprite in self.sprites:
            position = sprite.getPosition()
            position["y"] = position["y"] - moves
            sprite.moveTo(position["x"], position["y"])

    def moveDownBy(self,moves):
        for sprite in self.sprites:
            position = sprite.getPosition()
            position["y"] = position["y"] + moves
            sprite.moveTo(position["x"], position["y"])

    #Another option for how to move
    def moveToX(self, newX):
        for sprite in self.sprites:
            position = sprite.getPosition()
            sprite.moveTo(newX, position["y"])

    def moveToY(self, newY):
        for sprite in self.sprites:
            position = sprite.getPosition()
            sprite.moveTo(position["x"], newY)


class Wall(GroupOfSprites):
    def __init__(self, listOfCoordinates, brightness):
        GroupOfSprites.__init__(self, listOfCoordinates, brightness)

    def takeDamage(self, coordinatesHit, brightnessLost):
        for sprite in self.sprites:
            position = sprite.getPosition()
            index = 0
            while(index < len(coordinatesHit)):
                if(coordinatesHit[index]["x"] == position["x"] and coordinatesHit[index]["y"] == position["y"]):
                    sprite.loseBrightness(brightnessLost)
                index += 1
