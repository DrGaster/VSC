Num = int(input("Whole Number? "))

# -1 or less
def measu(n):
    if n <= -1:
        return "LO"
    # 0 or greater, less than 10

    elif 0 <= n < 10:
        return "MI"
    # greater than or equal to 10

    else: ## n >= 10:
        return "HI"
        
    #number in, return number

print(measu(Num))