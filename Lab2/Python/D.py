a, b, c, d = map(int, input().split())
if a < 0:
    a, b, c, d = -a, -b, -c, -d
def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d
l, r = -2000.0, 2000.0
for _ in range(200):
    m = (l + r) / 2
    if f(m) < 0:
        l = m
    else:
        r = m
print(f"{(l + r) / 2:.6f}")
