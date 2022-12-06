

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
    
    def move(self,x,y):
        self.xCoord = x
        self.yCoord = y
    
    def getCurrentPosition(self):
        return {"x":self.xCoord, "y":self.yCoord}

    

    
