nums = [5, 9, 4, 6, 2, 7, 4, 5, 1, 3, 2]

def recsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        a = recsort(arr[:len(arr)//2])
        b = recsort(arr[len(arr)//2:])
        return recsortHelper(a, b)
    
def recsortHelper(a, b):
    sorted = []
    while len(a) != 0 and len(b) != 0:
        if a[0] > b[0]:
            sorted.append(b[0])
            b.remove(b[0])
        else:
            sorted.append(a[0])
            a.remove(a[0])
    sorted.extend(b)
    sorted.extend(a)
    return sorted

def cocksort(arr):
    for y in range(len(arr)):
        if y%2 == 0:
            for x in range(len(arr)-1):
                if arr[x] > arr[x+1]:
                    a = arr[x]
                    b = arr[x+1]
                    arr[x] = b
                    arr[x+1] = a
        else:
            for x in range((len(arr)-1), 0, -1):
                if arr[x] < arr[x-1]:
                    a = arr[x]
                    b = arr[x-1]
                    arr[x] = b
                    arr[x-1] = a
    return arr

print(recsort(nums))
print(cocksort(nums))