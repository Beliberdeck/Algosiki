n = int(input())
a = [1, 2]
for k in range(3, n + 1):
    p = (k - 1) // 2
    old = a[p]
    a[p] = k
    a.append(old)
print(*a)
