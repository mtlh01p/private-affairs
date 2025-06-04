T = int(input())
for i in range(T):
    ans = 0
    X = int(input())
    for j in range(1, X+1):
        j_bin = len(bin(j))-2
        div = X//j
        div_bin = len(bin(div))-2
        if div_bin <= j_bin:
            ans += 1
    print(ans)

