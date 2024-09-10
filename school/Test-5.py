pattern_width = 0
while pattern_width == 0:
    pattern_width_req = input("Please enter pattern width: ")
    if pattern_width_req.isnumeric() and int(pattern_width_req) != 0:
        pattern_width = int(pattern_width_req)
    elif pattern_width_req.isnumeric():
        print("You do not want to do anything it seems.")
        break
    else:
         print("Hey pattern width must be a NUMBER!")

for y in range(pattern_width):
    for x in range(y+1):
        print("* ",end="")
    print('\n')

for y in range(pattern_width-2, 0, -1):
    for x in range(y+1):
        print("* ",end="")
    print('\n')
    