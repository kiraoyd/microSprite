from Sprite import *

class GroupOfSprites:
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





#test Main

list = [{"x":2, "y":2}, {"x":2, "y":3}, {"x":2, "y":4}, {"x":1, "y":2}, {"x":1, "y":1}]
group = GroupOfSprites(list, 9)
group.appear()
sleep(100)
group.vanish()
group.moveLeftBy(1)
group.appear()
