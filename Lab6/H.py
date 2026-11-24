import sys
from collections import deque

numbers = sys.stdin.read().split()
n = int(numbers[0])

matrix = []
for row_index in range(n):
    begin = 1 + row_index * n
    matrix.append(numbers[begin:begin + n])

start = int(numbers[1 + n * n]) - 1
finish = int(numbers[2 + n * n]) - 1

NOT_VISITED = -2
predok = [NOT_VISITED] * n
predok[start] = -1                     

queue = deque([start])                  
while queue:
    current = queue.popleft()
    for neighbor in range(n):
        if matrix[current][neighbor] == '1' and predok[neighbor] == NOT_VISITED:
            predok[neighbor] = current  
            queue.append(neighbor)

if predok[finish] == NOT_VISITED:
    print(-1)                           
elif start == finish:
    print(0)                            
else:
    path = []
    current = finish
    while current != -1:                
        path.append(current + 1)
        current = predok[current]
    path.reverse()                      
    print(len(path) - 1)                
    print(*path)