#include <iostream>
#include <vector>
using namespace std;

vector<int> insertionSort(vector<int> v) {
    int n = v.size();
    for (int i = 1; i < n; i++) {
        int val = v[i];
        int k = i - 1;
        while (k >= 0 && v[k] > val) {
            v[k + 1] = v[k];
            k--;
        }
        v[k + 1] = val;
    }
    return v;
}

int main() {
    vector<int> v;
    int x;
    while (cin >> x) {
        v.push_back(x);
    }
    v = insertionSort(v);
    for (size_t i = 0; i < v.size(); i++) {
        cout << v[i];
        if (i + 1 < v.size()) {
            cout << " ";
        }
    }
    cout << endl;

    return 0;
}
