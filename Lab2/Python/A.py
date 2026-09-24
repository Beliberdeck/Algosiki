def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
for x in b:
    res.append("YES" if binary_search(a, x) else "NO")

print("\n".join(res))
