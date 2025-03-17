while True:
    size_val = False
    while size_val == False:
        size_in = input("Enter how many bits: ")
        if size_in.isnumeric() and int(size_in) >= 1:
            size = int(size_in)
            size_val = True
        else:
            print("Enter the right binary size.")

    bin = []

    def convert(num):
        s = []
        while num > 0:
            if num % 2 == 0:
                s.insert(0, '0')
            else:
                s.insert(0, '1')
            num = num//2
        if len(s) < size:
            for x in range(size-len(s)):
                s.insert(0, '0')
        return(''.join(s))
    binfil = []
    if size == 1:
        bin.append(0)
        bin.append(1)
    else:
        for x in range(1, 2**size):
            bin.append(convert(x))
        for y in range(len(bin)):
            conseczeros = False
            for z in range(size-1):
                if bin[y][z] == '0' and bin[y][z+1] == '0':
                    conseczeros = True
                    break
            if not conseczeros:
                binfil.append(bin[y])

    for t in range(len(binfil)):
        print(binfil[t])
    