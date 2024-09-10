layer = 0
ship1_len, ship2_len = 0, 0
ship1_alg, ship2_alg = "", ""
ship1_alg_val, ship2_alg_val = False, False
ship_alg_allow = ["vertical", "horizontal"]
welmes = "Welcome to Battleships! Hit ENTER to continue."
inputreq1 = "Player 1, enter your coordinate to attack Player 2: "
inputreq2 = "Player 2, enter your coordinate to attack Player 1: "
inta = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
intb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
intc = ['0', '1']
ship1_coord = []

while ship1_len < 1 or ship1_len > 4:
    ship1_len = int(input("Player 1, enter your ship length: "))
while ship2_len < 1 or ship2_len > 4:
    ship2_len = int(input("Player 2, enter your ship length: "))

while ship1_alg_val == False:
    ship1_alg = input("Player 1, enter how you align your ship, 'vertical' or 'horizontal': ")
    if ship1_alg in ship_alg_allow:
        ship1_alg_val = True
while ship2_alg_val == False:
    ship2_alg = input("Player 2, enter how you align your ship, 'vertical' or 'horizontal': ")
    if ship2_alg in ship_alg_allow:
        ship2_alg_val = True

unfound1a = True
unfound1b = True
unfound1c = True
index1a = 0
index1b = 0
while unfound1a or unfound1b or unfound1c:
    in1a, in1b, in1c= [x for x in input("Player 1, enter your coordinate to place ship: ").split(',')]
    for x in range(len(inta)):
        if inta[x] == in1a:
            if (x + ship1_len) <= len(inta):
                unfound1a = False
                index1a = x
        if intb[x] == in1b:
            if (x + ship1_len) <= len(intb):
                unfound1b = False
                index1b = x
    for x in range(len(intc)):
        if intc[x] == in1c:
            unfound1c = False

if ship1_alg == "horizontal":
    num_added = 0
    for x in range(index1a, (index1a+ship1_len), 1):
        coord_adding = inta[x] + "," + in1b + "," + in1c
        ship1_coord.append(coord_adding)
else:
    num_added = 0
    for x in range(index1b, (index1b+ship1_len), 1):
        coord_adding = in1a + "," + intb[x] + "," + in1c
        ship1_coord.append(coord_adding)
print(ship1_coord)

ship2_validity = False
while ship2_validity == False:
    unfound2a = True
    unfound2b = True
    unfound2c = True
    index2a = 0
    index2b = 0
    ship2_temporary = []
    while unfound2a or unfound2b or unfound2c:
        in2a, in2b, in2c= [x for x in input("Player 2, enter your coordinate to place ship: ").split(',')]
        for x in range(len(inta)):
            if inta[x] == in2a:
                if (x + ship2_len) <= len(inta):
                    unfound2a = False
                    index2a = x
            if intb[x] == in2b:
                if (x + ship2_len) <= len(intb):
                    unfound2b = False
                    index2b = x
        for x in range(len(intc)):
            if intc[x] == in2c:
                unfound2c = False
    if ship2_alg == "horizontal":
        num_added = 0
        for x in range(index2a, (index2a+ship2_len), 1):
            coord_adding = inta[x] + "," + in2b + "," + in2c
            ship2_temporary.append(coord_adding)
    else:
        num_added = 0
        for x in range(index2b, (index2b+ship2_len), 1):
            coord_adding = in2a + "," + intb[x] + "," + in2c
            ship2_temporary.append(coord_adding)
    for x in range(len(ship2_temporary)):
        if ship2_temporary[x] in ship1_coord:
            print("Nope, Player 1 already preoccupies the coordinates!")
            break
    else:
        ship2_coord = ship2_temporary[:]
        ship2_validity = True
print(ship2_temporary)
print(ship2_coord)

while True:
    attack1 = input(inputreq1)
    attacked1 = ""
    for x in range(len(ship2_coord)):
        if attack1 == ship2_coord[x]:
            attacked1 = attack1
            ship2_coord[x] = ""
    if attacked1 != "":
        print("Attack successful!!!!!")
        ship2_len -= 1
    else:
        print("Ouch!!!!!!! What a fail¬")

    if ship2_len == 0:
        break

    attack2 = input(inputreq2)
    attacked2 = ""
    for x in range(len(ship1_coord)):
        if attack2 == ship1_coord[x]:
            attacked2 = attack2
            ship1_coord[x] = ""
    if attacked2 != "":
        print("Attack successful!!!!!")
        ship1_len -= 1
    else:
        print("Ouch!!!!!!! What a fail¬")
    
    if ship1_len == 0:
        break

if ship1_len == 0:
    print("Player 2 wins! Pulo Gadung to Monumen Nasional FTW")
else:
    print("Player 1 wins! We love you Blok M to Kota (f for respect to Kali Besar Barat)")