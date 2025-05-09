#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long factorial(int n) {
    long long result = 1;
    for (int i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<int> nums(N);
        for (int j = 0; j < N; j++) {
            nums[j] = j + 1;
        }
        
        int maxVal = 1; // Initialize maxVal with 1 (smallest possible value)

        // Process each permutation directly
        do {
            int Val = 0;
            // Calculate the 'Val' for this permutation
            for (int k = 0; k < N - 1; k++) {
                int dif = nums[k] - nums[k + 1];
                if (dif >= 0) {
                    Val += dif;
                } else {
                    Val -= dif;
                }
            }
            // Update maxVal if needed
            if (Val > maxVal) {
                maxVal = Val;
            }
        } while (next_permutation(nums.begin(), nums.end()));

        cout << maxVal << endl;
    }

    return 0;
}
