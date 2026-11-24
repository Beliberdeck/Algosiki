import sys

numbers = sys.stdin.read().split()
n = int(numbers[0])                     # вершин
m = int(numbers[1])                     # рёбер

neighbors = [[] for _ in range(n + 1)]
for i in range(m):
    a = int(numbers[2 + 2 * i])
    b = int(numbers[3 + 2 * i])
    neighbors[a].append(b)
    neighbors[b].append(a)              

visited = [False] * (n + 1)
visited[1] = True
stack = [1]                            
tree_edges = []                         

while stack:
    current = stack.pop()
    for neighbor in neighbors[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            stack.append(neighbor)
            tree_edges.append((current, neighbor))   

for a, b in tree_edges:
    print(a, b)