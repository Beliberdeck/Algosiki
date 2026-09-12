#include <iostream>
#include <vector>
using namespace std;

int BubbleSort(vector<int> a) {
    int n = a.size();
    int swaps = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
                swaps++;
            }
        }
    }
    return swaps;
}

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << BubbleSort(a) << endl;

    return 0;
}
