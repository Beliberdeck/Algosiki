#include <iostream>
using namespace std;

int main() {
    int n, x, y;
    cin >> n >> x >> y;
    int m = min(x, y);
    int l = m - 1, r = n * m;
    while (r - l > 1) {
        int t = l + (r - l) / 2;
        int a = (t - m) / x, b = (t - m) / y;
        if (a >= n - 1 - b) r = t; 
        else l = t;
    }
    cout << r;
}
