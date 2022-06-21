n = int(input("Whole Number? "))

# -1 or less
if n <= -1:
    print("LI")

# 0 or greater, less than 10
elif 0 <= n < 10:
    print("MI")

# greater than or equal to 10
else: ## n >= 10:
    print("HI")