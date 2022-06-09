# fruits task
# 09/06/2022

class fruit():
    def __init__(self, colour='unknown', size='unknown', taste='unknown'):
        self.colour = colour
        self.size = size
        self.taste = taste

    def printDescription(self):
        print('My colour is ' + self.colour + '\nMy size is ' + self.size + '\nMy taste is ' + self.taste)

class tropical(fruit):
    def __init__(self, colour, size, taste='sweet'):
        super().__init__(colour, size, taste)

class citrus(fruit):
    def __init__(self, colour, size, bitterLevel='unknown'):
        self.bitterLevel = bitterLevel
        super().__init__(colour, size, bitterLevel)
        
    def printDescription(self):
        print('My colour is ' + self.colour + '\nMy size is ' + self.size + '\nMy bitter level is ' + self.bitterLevel)

mango = tropical('red', 'medium')
mango.printDescription()

lemon = citrus('yellow', 'small', '8')
lemon.printDescription()
