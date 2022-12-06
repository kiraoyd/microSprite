

#How do we get the microbit code imported?

class Sprite:
    def __init__(self,startX, startY, brightness):
        self.__xCoord = startX
        self.__yCoord = startY
        self.__brightness = brightness


    def on(self):
        display.set_pixel(self.__xCoord, self.__yCoord, self.__brightness) #need to connect to microbit code

    def off(self):
        display.set_pixel(self.__xCoord, self.__yCoord, 0)
        
    def setBrightness(self, level):
        self.__brightness = level

    def move(self, x,y):
        self.__xCoord = x
        self.__yCoord = y

    def getCurrentPosition(self):
        return {"x":self.__xCoord, "y":self.__yCoord}
    
    #NEXT: how to deal with steps that take us out of bounds cleanly?
    def moveLeft(self, steps):
        self.spriteOff()
        if(self.xCoord - steps < self.xMin):
            self.xCoord = self.xMax + self.xCoord - steps+1
            print(self.xCoord)
        else:
            self.xCoord = self.xCoord - steps
        self.spriteOn()

    def moveRight(self, steps):
        self.spriteOff()
        self.xCoord = self.xCoord + steps
        self.spriteOn()

    def moveUp(self, steps):
        self.spriteOff()
        self.xCoord = self.yCoord + steps
        self.spriteOn()

    def moveDown(self, steps):
        self.spriteOff()
        self.xCoord = self.yCoord - steps
        self.spriteOn()

# I should have made a PR!