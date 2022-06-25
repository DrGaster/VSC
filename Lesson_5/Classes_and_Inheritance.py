import Block_data

    # @staticmethod
    # def time(day):
    #     if day.hour <= 12:
    #         return "Day"
    #     return "Night"

Ruby = Block_data.Block('Ruby', '2', '3', '1', 'pickaxe')
Coal = Block_data.Block('Block of Coal', '5', '6', '1', 'pickaxe')
Bucket_of_Water = Block_data.itemstack('Bucket of Water', '0', '0', '1', 'fist', 'liquid')
print(Ruby.__repr__())
print(Ruby.__str__())
# createblock = str(input("Name-Hardness-Resistance-Damage-Tooltype\n"))
# newblock = Block_data.fromstring(createblock)
# print(Ruby_Block.name)
# print(Coal_Block.name)

# print(Bucket_of_Water.name)

# import datetime

# the_time = datetime.time(11, 00)

# print(Block_data.time(the_time))

# print(Ruby.hardness)
# print(Coal.resistance)

# print(Ruby.damage)
# print(Ruby.getdamage())
# print(Ruby.setDamage('SKY BLUE'))
# print(Ruby.getdamage())
# print(Ruby.tooltype)
# print(Block_data.num_of_blocks)
# print('\n')
# print(newblock.damage)
# print(Block_data.damage(Ruby.damage))
# print(Block_data.hardness(Coal.hardness))

# print(Ruby.damage)
# print(Coal.hardness)

# print(1 + 2)
# print('1' + '2')
# print('a' + 'b')