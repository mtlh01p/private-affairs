def process_query(n):
    powers = []
    power = 0
    while n > 0:
        if n % 2 == 1:
            powers.append(3**power)
        n //= 2
        power += 1
    powers.sort()
    return powers

t = int(input())
for _ in range(t):
    n = int(input())
    subset = process_query(n)
    print(len(subset))
    print(" ".join(str(x) for x in subset))
