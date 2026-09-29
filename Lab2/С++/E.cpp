#include <iostream>
#include <vector>
using namespace std;

bool can(const vector<int>& x, int k, int d) {
    int cnt = 1, last = x[0];
    for (int i = 1; i < x.size(); i++)
        if (x[i] - last >= d) {
            cnt++;
            last = x[i];
        }
    return cnt >= k;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> x(n);
    for (int i = 0; i < n; i++) cin >> x[i];
    int l = 1, r = x[n - 1] - x[0] + 1;
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (can(x, k, m)) l = m;
        else r = m;
    }
    cout << l;
}
