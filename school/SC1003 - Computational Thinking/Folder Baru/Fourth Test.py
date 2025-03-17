def factorial(t):
    if int(t) == 0:
        return 1
    else:
        return int(t) * factorial(int(t)-1)

while True:
    p = input("What to factor? ")
    print(factorial(p))