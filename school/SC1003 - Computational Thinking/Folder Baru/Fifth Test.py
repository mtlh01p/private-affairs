def NumofLeaves(a):
    if len(a) == 1:
        return 1
    else:
        return (NumofLeaves(a[0]) + 1 + NumofLeaves(a[2]))

while True:
    r = input("Input a tree: [")
    f = r.split(", ")
    print("Number of Leaves: ", NumofLeaves(f))