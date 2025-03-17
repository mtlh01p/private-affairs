bin = [[[7], 5, [9]], 3, [[2], 8, [4]]]

def numOfNodes(tree):
    if len(tree[0]) > 1 and len(tree[2]) > 1:
        a = tree[0]
        b = tree[2]
        return numOfNodes(a) + 1 + numOfNodes(b)
    else:
        return len(tree)

def sumNodes(tree):
    f = sumNodesHelper(tree, 0)
    return f
    
def sumNodesHelper(tree, sum):
    if len(tree) == 1:
        sum = tree[0]
    else:
        a = sumNodesHelper(tree[0], sum)
        b = sumNodesHelper(tree[2], sum)
        sum = a + tree[1] + b
    return sum

def maxNodes(tree):
    f = maxNodesHelper(tree, 0)
    return f

def maxNodesHelper(tree, maks):
    if len(tree) == 1:
        maks = tree[0]
    else:
        a = maxNodesHelper(tree[0], maks)
        b = maxNodesHelper(tree[2], maks)
        maks = max(a, tree[1], b)
    return maks

def minNodes(tree):
    f = minNodesHelper(tree, 0)
    return f

def minNodesHelper(tree, minm):
    if len(tree) == 1:
        minm = tree[0]
    else:
        a = minNodesHelper(tree[0], minm)
        b = minNodesHelper(tree[2], minm)
        minm = min(a, tree[1], b)
    return minm

def mirror(tree):
    f = mirrorHelper(tree, [])
    return f

def mirrorHelper(tree, arr):
    if len(tree) == 1:
        arr = tree
    else:
        a = mirrorHelper(tree[0], arr)
        b = mirrorHelper(tree[2], arr)
        arr = [b, tree[1], a]
    return arr

def extract(tree):
    f = extractHelper(tree, [])
    return f

def extractHelper(tree, arr):
    if len(tree) == 1:
        arr.extend(tree)
    else:
        arr.append(tree[1])
        a = extractHelper(tree[0], arr)
        b = extractHelper(tree[2], arr)
    return arr
    
print("Number of leaves: ", numOfNodes(bin))
print("Sum of leaves: ", sumNodes(bin))
print("Max of leaves: ", maxNodes(bin))
print("Min of leaves: ", minNodes(bin))
print("Mirror of leaves: ", mirror(bin))
print("Extracts: ", extract(bin))
