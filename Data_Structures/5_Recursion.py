def recur_add(x):
    if x == 0:
        return 0
    else:
        return 1 + recur_add(x - 1)

print(recur_add(10))