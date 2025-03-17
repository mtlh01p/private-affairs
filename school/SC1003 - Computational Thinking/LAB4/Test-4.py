month = 0
numex25 = 0
temp = []
while month == 0:
    reqmonth = input("Enter number of days of the month: ")
    if reqmonth.isnumeric():
        month = int(reqmonth)
    else:
        print("Hey number of months must be a NUMBER!")

for x in range(month):
    temptoinput = 0
    temptoinput_val = False
    while temptoinput_val == False:
        message = "Temperature day " + str(x+1) + ": "
        temptoinputreq = input(message)
        if temptoinputreq.isnumeric():
            temptoinput = int(temptoinputreq)
            temptoinput_val = True
        else:
            print("Hey temp must be NUMBER!")
    temp.append(temptoinput)
    if temptoinput > 25.0:
        numex25 += 1

print("Number of days when temp exceeds 25*C is", numex25, "days.")