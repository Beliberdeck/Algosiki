def qick(a, start, end):
    if start < end:
        p = partition(a, start, end)
        qick(a, start, p - 1)
        qick(a, p + 1, end)


def partition(a, lbord, rbord):
    mid = (lbord + rbord) // 2
    a[mid], a[rbord] = a[rbord], a[mid]

    pivot = a[rbord]
    i = lbord - 1

    for j in range(lbord, rbord):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[rbord] = a[rbord], a[i + 1]
    return i + 1


n = int(input())
a = list(map(int, input().split()))

qick(a, 0, n - 1)
print(*a)
