import random
lebar = 4
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
selNums = []
win = False
play = False
attempt = 0

def genNumbers():
    global numList, selNums
    if len(selNums) != 0:
        selNums = []
    for x in range(lebar):
        f = random.choice(numList)
        selNums.append(f)

def userGuess():
    global win, lebar, selNums
    valid = False
    while valid == False:
        m = input("Please input 4 digits: ")
        if m.isnumeric() and len(m) == lebar:
            valid = True
    bulls = 0
    cows = 0
    for y in range(lebar):
        if int(m[y]) == selNums[y]:
            bulls += 1
        elif int(m[y]) in selNums:
            cows += 1
    if bulls == lebar:
        win = True
        print("You win!")
        print("You did ", attempt, "attempts.")
    else:
        print(bulls, "A and ", cows, "B")

while True:
    attempt = 0
    win = False
    play = False
    if play == False:
        genNumbers()
        play = True
    while play == True and win == False:
        attempt += 1
        userGuess()


    