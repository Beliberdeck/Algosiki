import sys

def sift_down(a, i, n):
    while True:
        l = 2 * i + 1
        if l >= n:
            break
        if l + 1 < n and a[l + 1] > a[l]:
            l += 1
        if a[l] > a[i]:
            a[l], a[i] = a[i], a[l]
            i = l
        else:
            break

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    for i in range(n // 2 - 1, -1, -1):
        sift_down(a, i, n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end)
    print(' '.join(map(str, a)))

main()
