import sys
from collections import deque

n, start_x, start_y, finish_x, finish_y = map(int, sys.stdin.read().split())

hody_konya = [(1, 2), (2, 1), (-1, 2), (-2, 1),
              (1, -2), (2, -1), (-1, -2), (-2, -1)]

predok = {(start_x, start_y): None}
queue = deque([(start_x, start_y)])

while queue:
    x, y = queue.popleft()
    if (x, y) == (finish_x, finish_y):
        break                          
    for dx, dy in hody_konya:
        new_x = x + dx
        new_y = y + dy
        inside = 1 <= new_x <= n and 1 <= new_y <= n
        if inside and (new_x, new_y) not in predok:
            predok[(new_x, new_y)] = (x, y)
            queue.append((new_x, new_y))

path = []
cell = (finish_x, finish_y)
while cell is not None:
    path.append(cell)
    cell = predok[cell]
path.reverse()

print(len(path) - 1)                   
for x, y in path:                       
    print(x, y)