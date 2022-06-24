class Block:

    tooltype = "Pickaxe"
    num_of_blocks = 0

    def __init__(self, name, hardness, resistance, color, tooltype):
        self.name = name
        self.hardness = hardness
        self.resistance = resistance
        self.color = color
        self.tooltype = tooltype

        Block.num_of_blocks += 1

    def empt(self,):
        pass

    def getColor(self): # Getter
        return self.color

    def setColor(self, newColor): # Setter
        self.color = newColor
        return "Color has been set to " + newColor

    @classmethod
    def light(cls, level):
        level = 0
    
    @classmethod
    def fromstring(cls, newblock):
        name, hardness, resistance, color, tooltype = newblock.split('-')
        return cls(name, hardness, resistance, color, tooltype)
    
    @staticmethod
    def time(day):
        if day.hour <= 12:
            return "Day"
        return "Night"
        


Ruby = Block('Ruby', '2', '3', 'Red', 'pickaxe')
Coal = Block('Block of Coal', '5', '6', 'Black', 'pickaxe')

# createblock = str(input("Name-Hardness-Resistance-Color-Tooltype\n"))
# newblock = Block.fromstring(createblock)
# print(Ruby_Block.name)
# print(Coal_Block.name)

import datetime

the_time = datetime.time(14, 00)

print(Block.time(the_time))

# print(Ruby.hardness)
# print(Coal.resistance)

# print(Ruby.color)
# print(Ruby.getColor())
# print(Ruby.setColor('SKY BLUE'))
# print(Ruby.getColor())
# print(Ruby.tooltype)
# print(Block.num_of_blocks)
# print('\n')
# print(newblock.color)
# print(Block.color(Ruby.color))
# print(Block.hardness(Coal.hardness))

# print(Ruby.color)
# print(Coal.hardness)