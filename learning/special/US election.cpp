#include <iostream>
#include <string>
#include <vector>
using namespace std;

string state[50];
int electoral[50];
vector<string> current_combo;
int pose = 1;

void findCombinations(int index, int totalVotes) {
    if (totalVotes >= 270 && totalVotes <= 300) {
        cout << "COMBINATION " << pose++ << " (Total: " << totalVotes << "):" << endl;
        for (const string& s : current_combo) {
            cout << "  " << s << endl;
        }
        cout<< endl;
    }

    if (index == 50 || totalVotes > 300) return;
    current_combo.push_back(state[index]);
    findCombinations(index + 1, totalVotes + electoral[index]);
    current_combo.pop_back();
    findCombinations(index + 1, totalVotes);
}

int main() {
    for (int i = 0; i < 50; ++i) {
        cout << "Enter name of state #" << (i+1) << ": ";
        cin >> state[i];

        while (true) {
            cout << "How many electoral votes for " << state[i] << "? ";
            int ev;
            cin >> ev;
            if (cin.fail() || ev <= 0) {
                cin.clear();
                cin.ignore(10000, '\n');
                cout << "Invalid. Try again." << endl;
            } else {
                electoral[i] = ev;
                break;
            }
        }
    }

    findCombinations(0, 0);
    return 0;
}
