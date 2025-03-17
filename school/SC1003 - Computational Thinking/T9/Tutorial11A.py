x = ['a', 'b', 'c', 'd', 'e', 'i']

def length11(arr):
    if len(arr) != 0:
        return 1 + length11(arr[1:]) 
    return 0

def length12(arr):
    f = length12helper(arr, 0)
    return f

def length12helper(arr, num):
    if len(arr) == 1:
        num += 1
    else:
        num += 1
        k = length12helper(arr[1:], num)
        return k
    return num

def length13(arr):
    num = 0
    for a in arr:
        num += 1
    return num

def vowel21(arr):
    vowels = 'aiueoAIUEO'
    if len(arr) != 0:
        if arr[0] in vowels:
            return 1 + vowel21(arr[1:])
        else:
            return vowel21(arr[1:])
    return 0

def vowel22(arr):
    k = vowel22Helper(arr, 0)
    return k

def vowel22Helper(arr, num):
    vowels = 'aiueoAIUEO'
    if len(arr) == 1:
        if arr[0] in vowels:
            num += 1
    else:
        if arr[0] in vowels:
            num += 1
        c = vowel22Helper(arr[1:], num)
        return c
    return num

def vowel23(arr):
    vowels = 'aiueoAIUEO'
    num = 0
    for a in arr:
        if a in vowels:
            num += 1
    return num
    
print(length11(x))
print(length12(x))
print(length13(x))
print(vowel21(x))
print(vowel22(x))
print(vowel23(x))