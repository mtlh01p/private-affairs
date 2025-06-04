def get_num_bits(n):
    return n.bit_length()

def solve():
    X = int(input())
    low = 1
    high = X
    lower_lim = X 
    while low <= high:
        mid = low + (high - low) // 2
        bits_div = get_num_bits(X // mid)
        bits_j = get_num_bits(mid)
        if bits_div <= bits_j:
            lower_lim = mid
            high = mid - 1
        else:
            low = mid + 1
    ans = X - lower_lim + 1
    print(ans)

T = int(input())

for _ in range(T):
    solve()
