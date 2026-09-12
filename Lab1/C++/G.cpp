#include <iostream>
#include <vector>
using namespace std;

void CountSort(vector<int>& A) {
    vector<int> count(101, 0);
    for (int x : A) {
        count[x]++;
    }
    int idx = 0;
    for (int value = 0; value <= 100; value++) {
        for (int c = 0; c < count[value]; c++) {
            A[idx] = value;
            idx++;
        }
    }
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) A.push_back(x);
    CountSort(A);
    for (int i = 0; i < (int)A.size(); i++)
        cout << A[i] << (i + 1 < (int)A.size() ? " " : "\n");
    return 0;
}
