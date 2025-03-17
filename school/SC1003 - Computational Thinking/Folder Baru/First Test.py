import random
choose = ["A", "B", "C", "D", "E", "F"]
width = 3
chosen = []
guessed = False
attempts = 0

def guessr():
    global guessed, attempts
    r = input("Please input 4 characters:" )
    if len(r) == width:
        word = ''.join(chosen)
        if r == word:
            guessed = True
            print("Correct! You did ", attempts, " attempts. Play again?")
        else:
            cors = 0
            unpl = 0
            for x in range(width):
                if r[x] == chosen[x]:
                    cors += 1
                else:
                    for y in range(width-1):
                        if r[x] == chosen[y]:
                            unpl += 1
            print("You got ", cors, " letter(s) correctly placed and ", unpl, " letter(s) wrongly placed. Try again?")
            attempts += 1
    else:
        print("Oops, enter 4 characters! Not more, not less.")
        attempts += 1

while True:
    if guessed:
        guessed = False
    if attempts != 0:
        attempts = 0
    if len(chosen) != 0:
        chosen = []
    else:
        for x in range(width):
            n = random.choice(choose)
            chosen.append(n)
    
    while guessed == False:
        guessr()