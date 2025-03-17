req1 = input("Enter the number of boys: ")
req2 = input("Enter the number of girls: ")

def ohno():
    print("Enter a valid number of boys and girls. Must be a number.")

if req1.isnumeric() and req2.isnumeric():
    num_boys = int(req1)
    num_girls = int(req2)
    total = num_boys + num_girls
    print("Boys: " + str(round(num_boys/total*100)) + "%")
    print("Girls: " + str(round(num_girls/total*100)) + "%")
else:
    ohno()
    
