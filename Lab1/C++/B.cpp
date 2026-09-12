#include <iostream>
#include <vector>
using namespace std;

vector<int> insertionSort(vector<int> A) {
    int n = A.size();
    for (int i = 1; i < n; i++) {
        int val = A[i];
        int k = i - 1;
        while (k >= 0 && A[k] > val) {
            A[k + 1] = A[k];
            k--;
        }
        A[k + 1] = val;
    }
    return A;
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }
    A = insertionSort(A);
    for (size_t i = 0; i < A.size(); i++) {
        cout << A[i];
        if (i + 1 < A.size()) {
            cout << " ";
        }
    }
    cout << endl;
    return 0;
}
