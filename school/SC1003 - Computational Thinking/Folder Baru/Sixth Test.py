mytasklist = []
complstat = []

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Filter Tasks")

    choice = input("Enter your choice: ")

    if choice.isnumeric():
        if int(choice) == 1:
            comm = input("Pls add item: ")
            if comm != "":
                mytasklist.append(comm)
                complstat.append(False)
                print("Task added.")
            else:
                print("you entered an empty task?")
        elif int(choice) == 2:
            if len(mytasklist) != 0:
                for x in range(len(mytasklist)):
                    printing = mytasklist[x]
                    if complstat[x] == True:
                        print(mytasklist[x], " (DONE)")
                    else:
                        print(mytasklist[x])
            else:
                print("nothing")
        elif int(choice) == 3:
            comm = input("which one to edit: ")
            if comm in mytasklist:
                indx = mytasklist.index(comm)
                comm2 = input("replace with: ")
                if comm2 != "":
                    mytasklist[indx] = comm2
                    print("Task modified.")
                else:
                    print("no, use the correct command to delete")
            else:
                print("no such task in the list")
        elif int(choice) == 4:
            comm = input("which one to delete: ")
            if comm in mytasklist:
                indx = mytasklist.index(comm)
                mytasklist.remove(comm)
                print("Task removed.")
            else:
                print("no such task in the list")
        elif int(choice) == 5:
            comm = input("which one you've done: ")
            if comm in mytasklist:
                indx = mytasklist.index(comm)
                complstat[indx] = True
                print("Task marked as done.")
            else:
                print("no such task in the list")
        elif int(choice) == 6:
            if len(mytasklist) != 0:
                pending = []
                done = []
                for x in range(len(mytasklist)):
                    if complstat[x] == True:
                        done.append(mytasklist[x])
                    else:
                        pending.append(mytasklist[x])
                print("PENDING: ")
                for y in range(len(pending)):
                    print(pending[y])
                print(" ")
                print("DONE: ")
                for z in range(len(done)):
                    print(done[z])
            else:
                print("nothing")
        else:
            print("No, enter the correct number.")
    else:
        print("Pls just enter the number of command.")