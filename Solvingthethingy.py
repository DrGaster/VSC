NumVar1 = int(input("What is variable X? "))
NumVar2 = int(input("What is variable Y? "))

def expr(x, y):
    return (x + y)**2 - (y - x)**3

product = expr(NumVar1, NumVar2)
print(product)