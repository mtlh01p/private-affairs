import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    A = [int(num_str) for num_str in input().split()]
    
    xor_values_count = {}
    for k in range(1, N + 1):
        current_xor_val = A[k-1] ^ k
        xor_values_count[current_xor_val] = xor_values_count.get(current_xor_val, 0) + 1
    
    total_pairs = 0
    for count in xor_values_count.values():
        if count >= 2:
            total_pairs += count * (count - 1) // 2
            
    print(total_pairs)

T = int(input())
for _ in range(T):
    solve()
