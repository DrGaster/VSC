# n

# 1
# 22
# 333
# 4444
# 55555
# ...
# nnnnnnnnn

# level = int(input("How many levels? "))
# def pyr(num):
#     for num in range(5):
#         return str(num) * num
# pyrx = pyr(level)
# print(pyrx)

# def pyra(type, num):
#     for num in range(5):
#         return 4


# temp = []


# def pyra(num):
#     levelvar = int(input("Levels? "))
#     temp = list(range(levelvar))
#     for ent in temp:
#         return str(ent) * ent
#     # return str(levelvar) * levelvar
#     # print(temp)
# # pyr = p
# print(pyra(5))

def pyra(level):
    for i in range(level + 1):
        print(str(i) * i)

levelInput = int(input("How many levels? "))
pyra(levelInput)

