import sys

tokens = sys.stdin.read().split()
rows = int(tokens[0])                   
cols = int(tokens[1])                   
grid = tokens[2:2 + rows]               

visited = [[False] * cols for _ in range(rows)]
pieces = 0                              

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for start_row in range(rows):
    for start_col in range(cols):
        if grid[start_row][start_col] == '#' and not visited[start_row][start_col]:
            pieces += 1
            visited[start_row][start_col] = True
            stack = [(start_row, start_col)]

            while stack:
                row, col = stack.pop()
                for dr, dc in moves:
                    new_row = row + dr
                    new_col = col + dc
                    inside = 0 <= new_row < rows and 0 <= new_col < cols
                    if inside and grid[new_row][new_col] == '#' and not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        stack.append((new_row, new_col))

print(pieces)