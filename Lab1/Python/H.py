class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))
points.sort(key=lambda p: p.x ** 2 + p.y ** 2)
for p in points:
    print(p.x, p.y)
