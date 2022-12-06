#How do we get the microbit code imported?

class Sprite:
    def __init__(self,startX, startY, brightness):
        self.__xCoord = startX
        self.__yCoord = startY
        self.__brightness = brightness
        self.__xMax = 4
        self.__yMax = 4
        self.__xMin = 0
        self.__yMin = 0

    def spriteOn(self):
        display.set_pixel(self.__xCoord, self.__yCoord, self.__brightness) #need to connect to microbit code

    def spriteOff(self):
        display.set_pixel(self.__xCoord, self.__yCoord, 0)
        
    def setBrightness(self, level):
        self.__brightness = level
    
    #NEXT: how to deal with steps that take us out of bounds cleanly?
    def moveLeft(self, steps):
        self.spriteOff()
        if(self.__xCoord - steps < self.__xMin):
            self.__xCoord = self.__xMax + self.__xCoord - steps+1
            print(self.__xCoord)
        else:
            self.__xCoord = self.__xCoord - steps
        self.spriteOn()

    def moveRight(self, steps):
        self.spriteOff()
        self.__xCoord = self.__xCoord + steps
        self.spriteOn()

    def moveUp(self, steps):
        self.spriteOff()
        self.__xCoord = self.__yCoord + steps
        self.spriteOn()

    def moveDown(self, steps):
        self.spriteOff()
        self.__xCoord = self.__yCoord - steps
        self.spriteOn()

# I should have made a PR!