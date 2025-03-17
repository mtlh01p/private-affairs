def merge_sort(data, key):
    """
    BUBBLE SORT
    if type(data[0][key]) == str:
        for x in range(len(data)):
            for y in range(x+1, len(data)):
                if data[x][key][0] > data[y][key][0]:
                    r = data[x]
                    t = data[y]
                    data[x] = t
                    data[y] = r
    else:
        for x in range(len(data)):
            for y in range(x+1, len(data)):
                if data[x][key] > data[y][key]:
                    r = data[x]
                    t = data[y]
                    data[x] = t
                    data[y] = r
    """
    if len(data) > 1:
        a = data[:(len(data)//2)]
        b = data[(len(data)//2):]
        a = merge_sort(a, key)
        b = merge_sort(b, key)
        return merge(a, b, key)
    else:
        return data

def merge(left, right, key):
    sorted = []
    while len(left) != 0 and len(right) != 0:
        if type(left[0][key]) == str:
            strl = left[0][key][0]
            strr = right[0][key][0]
        else:
            strl = left[0][key]
            strr = right[0][key]

        if strl > strr:
            sorted.append(right[0])
            right.remove(right[0])
        else:
            sorted.append(left[0])
            left.remove(left[0])
    
    sorted.extend(left)
    sorted.extend(right)
    return sorted

persons = [
    {"name": "Bob", "age": 15}, 
    {"name": "Alice", "age": 12}, 
    {"name": "Elena", "age": 14},
    {"name": "Dave", "age": 13}, 
    {"name": "Carol", "age": 10},
]

sorted_data = merge_sort(persons, "name")
for index, person in enumerate(sorted_data):
    print(f"[{index+1}] Name: {person['name']}   \tAge: {person['age']}")