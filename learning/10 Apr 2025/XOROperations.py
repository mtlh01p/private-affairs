T = int(input())
for i in range(T):
    N = int(input())
    A_in = input()
    A = []
    for num_str in A_in.split():
        A.append(int(num_str))
    A = sorted(A)
    j = 1
    while True:
        ans = []
        for k in range(N):
            ans.append(A[k] ^ j)
        if sorted(ans) == A:
            break
        else:
            j += 1
    print(j)
