T = int(input())
for i in range(T):
    ans = 0
    X = int(input())
    lower_lim = 0
    for j in range(1, X+1):
        j_bin = len(bin(j))-2
        div = X//j
        div_bin = len(bin(div))-2
        if div_bin <= j_bin:
            ans += 1
            lower_lim = j
            break
    ans += X-lower_lim
    print(ans)


