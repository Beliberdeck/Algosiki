#include <iostream>
#include <vector>
using namespace std;

vector<int> SelectionSort(vector<int> A) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        int maxIndex = i;
        for (int j = i; j < n; j++) {
            if (A[j] > A[maxIndex]) {
                maxIndex = j;
            }
        }
        swap(A[i], A[maxIndex]);
    }
    return A;
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) A.push_back(x);

    A = SelectionSort(A);

    for (int i = 0; i < (int)A.size(); i++)
        cout << A[i] << (i + 1 < (int)A.size() ? " " : "\n");

    return 0;
}
