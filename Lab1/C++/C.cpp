#include <iostream>
#include <vector>
using namespace std;

vector<int> BubbleSort(vector<int> A) {
    int n = A.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (A[j] < A[j + 1]) {
                swap(A[j], A[j + 1]);
            }
        }
    }
    return A;
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) A.push_back(x);
    A = BubbleSort(A);
    for (int i = 0; i < (int)A.size(); i++)
        cout << A[i] << (i + 1 < (int)A.size() ? " " : "\n");
    return 0;
}
