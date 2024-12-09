board_size = 10
board = []
car_pos_val = False
sub_pos_val = False

while car_pos_val == False:
    print("Pls enter start_pos of Carrier in format (row,col). e.g. 6,4")
    car_pos = input("Enter coordinates: ")
    car_pos1 = car_pos.split(",")
    valstr = 0
    for x in range(len(car_pos1)):
        if car_pos1[x].isnumeric() and 0 <= int(car_pos1[x]) <= 9:
            car_pos1[x] = int(car_pos1[x])
            valstr += 1
    if valstr == 2:
        car_pos_val = True
    else:
        print("Invalid format.")
        
while sub_pos_val == False:
    print("Pls enter start_pos of Submarine in format (row,col). e.g. 6,4")
    sub_pos = input("Enter coordinates: ")
    sub_pos1 = sub_pos.split(",")
    valstr = 0
    for x in range(len(sub_pos1)):
        if sub_pos1[x].isnumeric() and 0 <= int(sub_pos1[x]) <= 9:
            sub_pos1[x] = int(sub_pos1[x])
            valstr += 1
    if valstr == 2:
        sub_pos_val = True
    else:
        print("Invalid format.")
    
ship = {
    "name": "Shipper",
    "carlength": 5,
    "sublength": 3,
    "carstart": car_pos1,
    "substart": sub_pos1,
}

for x in range(board_size):
    row = []
    for y in range(board_size):
        row.append(0)
    board.append(row)

def place_ship(ship_name):
    global board
    if ship_name == "Carrier":
        for y in range(car_pos1[1], car_pos1[1]+ship["carlength"]):
            if y <= 9:
                board[car_pos1[0]][y] = "S"
    elif ship_name == "Submarine":
        for y in range(sub_pos1[1], sub_pos1[1]+ship["sublength"]):
            if y <= 9:
                board[sub_pos1[0]][y] = "S"

place_ship("Carrier")
place_ship("Submarine")


att_row_val = False
att_col_val = False
att_row = -1
att_col = -1
while att_row_val == False or att_col_val == False: 
    att_row_in = input("Enter attack row: ")
    att_col_in = input("Enter attack column: ")
    if att_row_in.isnumeric() and 0 <= int(att_row_in) <= 9:
        att_row = int(att_row_in)
        att_row_val = True
    if att_col_in.isnumeric() and 0 <= int(att_col_in) <= 9:
        att_col = int(att_col_in)
        att_col_val = True
    if att_row_val == -1 or att_row_val == -1:
        print("Coordinates (", att_row_in, ", ", att_col_in, "are valid: False")
    else:
        print("Coordinates (", att_row_in, ", ", att_col_in, "are valid: True")
        board[att_row][att_col] = 1

for x in range(board_size):
    for y in range(board_size):
        if y != 9:
            print(board[x][y], end=' ')
        else:
            print(board[x][y], end=' \n')