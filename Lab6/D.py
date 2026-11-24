import sys

numbers = sys.stdin.read().split()
n = int(numbers[0])
start = int(numbers[1]) - 1

matrix = []
for row_index in range(n):
    begin = 2 + row_index * n           
    matrix.append(numbers[begin:begin + n])     

visited = [False] * n
visited[start] = True
stack = [start]                        
count = 0

while stack:
    current = stack.pop()               
    count += 1
    for neighbor in range(n):
        if matrix[current][neighbor] == '1' and not visited[neighbor]:
            visited[neighbor] = True
            stack.append(neighbor)

print(count)