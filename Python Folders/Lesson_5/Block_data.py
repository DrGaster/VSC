print("Imported Block Module.")


class Block:

    tooltype = "Pickaxe"
    num_of_blocks = 0
    damage = 1

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

    def getDamage(self): # Getter
        return self.damage

    def setDamage(self, newDamage): # Setter
        self.damage = newDamage
        return "Damage has been set to " + newDamage


    @classmethod
    def light(cls, level):
        level = 0
    
    @classmethod
    def fromstring(cls, newblock):
        name, hardness, resistance, damage, tooltype = newblock.split('-')
        return cls(name, hardness, resistance, damage, tooltype)


class itemstack(Block):
    def __init__(self, name, hardness, resistance, damage, tooltype, state):
        super().__init__(name, hardness, resistance, damage, tooltype)
        self.state = state