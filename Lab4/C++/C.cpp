#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<long long> h;

void push(long long x) {
    h.push_back(x);
    size_t i = h.size() - 1;
    while (i > 0 && h[(i - 1) / 2] > h[i]) {
        swap(h[(i - 1) / 2], h[i]);
        i = (i - 1) / 2;
    }
}

long long pop() {
    long long res = h[0];
    h[0] = h.back();
    h.pop_back();
    size_t n = h.size(), i = 0;
    while (true) {
        size_t l = 2 * i + 1, r = l + 1, m = i;
        if (l < n && h[l] < h[m]) m = l;
        if (r < n && h[r] < h[m]) m = r;
        if (m == i) break;
        swap(h[i], h[m]);
        i = m;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            h.clear();
        } else if (cmd == "ADD") {
            long long x;
            cin >> x;
            push(x);
        } else if (cmd == "EXTRACT") {
            if (h.empty()) cout << "CANNOT\n";
            else cout << pop() << "\n";
        }
    }
    return 0;
}
