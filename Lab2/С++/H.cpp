#include <iostream>
using namespace std;

int main() {
    int w, h, n;
    cin >> w >> h >> n;
    int l = 0, r = 31623 * max(w, h);
    while (r - l > 1) {
        int s = l + (r - l) / 2;
        if ((s / w) * (s / h) >= n) r = s;
        else l = s;
    }
    cout << r;
}
