board_size = 10
while True:
    cor_inval = True
    while cor_inval:
        row_inval = True
        while row_inval:
            attack_row = input("Enter attack row (0-9): ")
            if attack_row.isnumeric():
                attack_row = int(attack_row)
                row_inval = False
            else:
                print("Invalid row entered. It must be a WHOLE NUMBER!")
        col_inval = True
        while col_inval:
            attack_col = input("Enter attack column (0-9): ")
            if attack_col.isnumeric():
                attack_col = int(attack_col)
                col_inval = False
            else:
                print("Invalid column entered. It must be a WHOLE NUMBER!")
        if 0 <= attack_row <= 9 and 0 <= attack_col <= 9:
            msg = "Coordinates (" + str(attack_row) + ", " + str(attack_col) + ") are valid: True"
            print(msg)
            cor_inval = False
        else:
            msg = "Coordinates (" + str(attack_row) + ", " + str(attack_col) + ") are valid: False"
            print(msg)
            print("Please enter again.")

    for x in range(10):
        for y in range(10):
            if x == attack_row and y == attack_col:
                print("1", end=" ")
            else:
                print("0", end=" ")
            if y == 9:
                print("\n")
