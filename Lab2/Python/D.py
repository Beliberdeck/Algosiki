C = float(input())
left, right = 0.0, 100000.0
for _ in range(100):
    mid = (left + right) / 2
    if mid ** 2 + mid ** 0.5 < C:
        left = mid
    else:
        right = mid
print(f"{right:.6f}")
