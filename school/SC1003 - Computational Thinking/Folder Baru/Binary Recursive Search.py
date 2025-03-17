n = [0, 7, 14, 8, 5, 3, 2]

def instant(sch):
    return n.index(int(sch))

def binsort(n):
    if len(n) <= 1:
        return n
    else:
        a = binsort(n[:len(n)//2])
        b = binsort(n[len(n)//2:])
        n = binsortHelper(a, b)
        return n

def binsortHelper(a, b):
    sord = []
    while len(a) != 0 and len(b) != 0:
        if a[0] > b[0]:
            sord.append(b[0])
            b.remove(b[0])
        else:
            sord.append(a[0])
            a.remove(a[0])
    sord.extend(a)
    sord.extend(b)
    return sord

def binaryinit():
    global n
    n = binsort(n)
    print(n)

print(instant(7))