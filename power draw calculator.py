CPU=int(input("CPU: "))
GPU=int(input("GPU: "))
MEM=int(input("Memory bandwidth: "))
PCN=input("Process node: ")

while True:
    if PCN == "5nm":
        CPUp = CPU/7600 * 13 * 172/199
        GPUp = GPU/81 * 6 * 172/199
        MEMp = MEM/300 * 1
        print("Power: ", CPUp+GPUp+MEMp)
    elif PCN == "3nm":
        CPUp = CPU/7600 * 13 * 172/270
        GPUp = GPU/81 * 6 * 172/270
        MEMp = MEM/300 * 0.8
        print("Power: ", CPUp+GPUp+MEMp)
    else:
        print("Enter correct PCN. The choices are 5nm or 3nm.")