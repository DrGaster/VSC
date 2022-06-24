class Block:

    color = 'RANDOM COLOR'

    def __init__(self, name, hardness, resistance, color):
        self.name = name
        self.hardness = hardness
        self.resistance = resistance
        self.color = color

    def empt(self,):
        pass

    def getColor(self): # Getter
        return self.color

    def setColor(self, newColor): # Setter
        self.color = newColor
        return "Color has been set to " + newColor

    # def color(color1):
    #     return "I am trying to call this function! " + color1

    # def hardness(value):
    #     return "Hardness is: " + value

Ruby = Block('Ruby', '2', '3', 'Red')
Coal = Block('Block of Coal', '5', '6', 'Black')

# print(Ruby_Block.name)
# print(Coal_Block.name)

print(Ruby.hardness)
print(Coal.resistance)

print(Ruby.color)
print(Ruby.getColor())
print(Ruby.setColor('SKY BLUE'))
print(Ruby.getColor())

# print(Block.color(Ruby.color))
# print(Block.hardness(Coal.hardness))

# print(Ruby.color)
# print(Coal.hardness)