#How do we get the microbit code imported?

class Sprite:
    def __init__(self,startX, startY, brightness):
        self.xCoord = startX
        self.yCoord = startY
        self.brightness = brightness
        self.xMax = 4
        self.yMax = 4
        self.xMin = 0
        self.yMin = 0

    def spriteOn(self):
        display.set_pixel(self.xCoord, self.yCoord, self.brightness) #need to connect to microbit code

    def spriteOff(self):
        display.set_pixel(self.xCoord, self.yCoord, 0)
        
    def setBrightness(self, level):
        self.brightness = level
    
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