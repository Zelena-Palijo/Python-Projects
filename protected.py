

class Protected:
    def __init__(self):
        self.__privateVar = 1

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(25)
obj.getPrivate()
        
## result should be 1 and 5
