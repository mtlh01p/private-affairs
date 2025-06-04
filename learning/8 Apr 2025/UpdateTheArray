#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>

int minUpdates(int N, const std::vector<int>& A, int K) {
    if (N % 2 != 0) {
        return -1;
    }

    int operations = 0;
    int target_parity_count = N / 2;
    std::map<int, int> initial_counts;
    for (int x : A) {
        initial_counts[x]++;
    }

    std::set<int> kept_values_from_A;
    int current_odd_count = 0;
    int current_even_count = 0;

    std::map<int, int> temp_counts = initial_counts;

    for (int i = 0; i < N; ++i) {
        int val = A[i];
        if (temp_counts[val] > 1 || val > K) {
            operations++;
            temp_counts[val]--; 
        } else {
            kept_values_from_A.insert(val);
            if (val % 2 != 0) {
                current_odd_count++;
            } else {
                current_even_count++;
            }
        }
    }

    if (current_odd_count > target_parity_count) {
        int excess_odds = current_odd_count - target_parity_count;
        std::vector<int> values_to_remove_from_kept;
        for (int val : kept_values_from_A) {
            if (excess_odds == 0) break;
            if (val % 2 != 0) {
                values_to_remove_from_kept.push_back(val);
                excess_odds--;
            }
        }
        for(int val : values_to_remove_from_kept) {
            kept_values_from_A.erase(val);
            current_odd_count--;
            operations++;
        }
    }

    if (current_even_count > target_parity_count) {
        int excess_evens = current_even_count - target_parity_count;
        std::vector<int> values_to_remove_from_kept;
        for (int val : kept_values_from_A) {
            if (excess_evens == 0) break;
            if (val % 2 == 0) {
                values_to_remove_from_kept.push_back(val);
                excess_evens--;
            }
        }
        for(int val : values_to_remove_from_kept) {
            kept_values_from_A.erase(val);
            current_even_count--;
            operations++;
        }
    }

    int needed_odd_from_k_pool = target_parity_count - current_odd_count;
    int needed_even_from_k_pool = target_parity_count - current_even_count;

    int available_odd_in_k = 0;
    int available_even_in_k = 0;

    for (int i = 1; i <= K; ++i) {
        if (kept_values_from_A.find(i) == kept_values_from_A.end()) {
            if (i % 2 != 0) {
                available_odd_in_k++;
            } else {
                available_even_in_k++;
            }
        }
    }

    if (needed_odd_from_k_pool > available_odd_in_k || needed_even_from_k_pool > available_even_in_k) {
        return -1;
    return operations;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int T;
    std::cin >> T;
    while (T--) {
        int N;
        std::cin >> N;
        std::vector<int> A(N);
        for (int i = 0; i < N; ++i) {
            std::cin >> A[i];
        }
        int K;
        std::cin >> K;

        int result = minUpdates(N, A, K);
        std::cout << result << "\n";
    }

    return 0;
}
