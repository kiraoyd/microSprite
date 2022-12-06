# micros:sprite
# by Kira K & Mike W

class Sprite:
    def __init__(self,startX, startY, brightness):
        self.__xCoord = startX
        self.__yCoord = startY
        self.__brightness = brightness

    def on(self):
        display.set_pixel(self.__xCoord, self.__yCoord, self.__brightness) 

    def off(self):
        display.set_pixel(self.__xCoord, self.__yCoord, 0)
        
    def setBrightness(self, level):
        self.__brightness = level

    def move(self, x,y):
        self.__xCoord = x
        self.__yCoord = y

    def getCurrentPosition(self):
        return {"x":self.__xCoord, "y":self.__yCoord}