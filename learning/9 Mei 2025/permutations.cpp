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
        vector<int> nums;
        for (int j = 1; j <= N; j++) {
            nums.push_back(j);
        }
        vector<vector<int>> permutations;

        do {
            vector<int> perm = nums; 
            permutations.push_back(perm); 
        } while (next_permutation(nums.begin(), nums.end()));
        
        int maxVal = 1;
        for(int j=0; j<permutations.size(); j++) {
            int Val = 0; 
            for(int k=0; k<N-1; k++) {
                int dif = permutations[j][k] - permutations[j][k+1];
                if(dif >= 0) {
                    Val += dif;
                }else{
                    Val -= dif;
                }
            }
            if(Val > maxVal) {
                maxVal = Val;
            }
        }
        cout << maxVal << endl;
    }

    return 0;
}