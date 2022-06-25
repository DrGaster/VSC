class Block:

    tooltype = "Pickaxe"
    num_of_blocks = 0

    def __init__(self, name, hardness, resistance, damage, tooltype):
        self.name = name
        self.hardness = hardness
        self.resistance = resistance
        self.damage = damage
        self.tooltype = tooltype

        Block.num_of_blocks += 1
    def __repr__(self) -> str:
        return "Block('{}', '{}', '{}', '{}', '{}')".format(self.name, self.hardness, self.resistance, self.damage, self.tooltype)

    def __str__(self):
        return "Block: {}\nHarvest Tool: {}".format(self.name, self.tooltype)

    def getColor(self): # Getter
        return self.damage

    def setColor(self, newColor): # Setter
        self.damage = newColor
        return "Color has been set to " + newColor

    @classmethod
    def light(cls, level):
        level = 0
    
    @classmethod
    def fromstring(cls, newblock):
        name, hardness, resistance, damage, tooltype = newblock.split('-')
        return cls(name, hardness, resistance, damage, tooltype)
    
    # @staticmethod
    # def time(day):
    #     if day.hour <= 12:
    #         return "Day"
    #     return "Night"

class temp():
    pass
class itemstack(Block):
    def __init__(self, name, hardness, resistance, damage, tooltype, state):
        super().__init__(name, hardness, resistance, damage, tooltype)
        self.state = state

Ruby = Block('Ruby', '2', '3', '1', 'pickaxe')
Coal = Block('Block of Coal', '5', '6', '1', 'pickaxe')
Bucket_of_Water = itemstack('Bucket of Water', '0', '0', '1', 'fist', 'liquid')
print(Ruby.__repr__())
print(Ruby.__str__())
# createblock = str(input("Name-Hardness-Resistance-Color-Tooltype\n"))
# newblock = Block.fromstring(createblock)
# print(Ruby_Block.name)
# print(Coal_Block.name)

# print(Bucket_of_Water.name)

# import datetime

# the_time = datetime.time(11, 00)

# print(Block.time(the_time))

# print(Ruby.hardness)
# print(Coal.resistance)

# print(Ruby.damage)
# print(Ruby.getColor())
# print(Ruby.setColor('SKY BLUE'))
# print(Ruby.getColor())
# print(Ruby.tooltype)
# print(Block.num_of_blocks)
# print('\n')
# print(newblock.damage)
# print(Block.damage(Ruby.damage))
# print(Block.hardness(Coal.hardness))

# print(Ruby.damage)
# print(Coal.hardness)

# print(1 + 2)
# print('1' + '2')
# print('a' + 'b')