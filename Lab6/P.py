import sys
from collections import deque

numbers = sys.stdin.read().split()
n = int(numbers[0])                     
m = int(numbers[1])                     

maze = []
for row_index in range(n):
    begin = 2 + row_index * m
    maze.append(list(map(int, numbers[begin:begin + m])))

dist = [[-1] * m for _ in range(n)]
dist[0][0] = 0                         
queue = deque([(0, 0)])

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    row, col = queue.popleft()
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        inside = 0 <= new_row < n and 0 <= new_col < m
        if inside and maze[new_row][new_col] == 0 and dist[new_row][new_col] == -1:
            dist[new_row][new_col] = dist[row][col] + 1
            queue.append((new_row, new_col))

print(dist[n - 1][m - 1])