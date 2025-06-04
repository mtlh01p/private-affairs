T = int(input())

def comp(a, b):
    return a^b

for i in range(T):
    nums = 0
    N = int(input())
    A_in = input()
    A = []
    for num_str in A_in.split():
        A.append(int(num_str))
    for i in range(1, N):
        for j in range(i+1, N+1):
            ans1 = comp(A[i-1], j)
            ans2 = comp(A[j-1], i)
            if ans1 == ans2:
                nums += 1
    print(nums)
