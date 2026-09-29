#include <iostream>
#include <vector>
using namespace std;

bool can(const vector<int>& a, int k, int L) {
    int cnt = 0;
    for (int x : a) {
        cnt += x / L;
        if (cnt >= k) return true;
    }
    return false;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int l = 0, r = 10000001;
    while (r - l > 1) {
        int m = l + (r - l) / 2;
        if (can(a, k, m)) l = m;
        else r = m;
    }
    cout << l;
}
