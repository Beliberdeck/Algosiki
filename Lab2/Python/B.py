def closest(arr, x):
    left, right = 0, len(arr) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid
        else:
            right = mid
    if x - arr[left] <= arr[right] - x:
        return arr[left]
    return arr[right]


n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for x in arr2:
    print(closest(arr1, x))
