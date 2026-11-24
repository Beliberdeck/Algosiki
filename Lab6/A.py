import sys

numbers = sys.stdin.read().split()
size = int(numbers[0])                 

matrix = []
for row_index in range(size):
    begin = 1 + row_index * size        
    row = list(map(int, numbers[begin:begin + size]))
    matrix.append(row)

is_ok = True
for i in range(size):
    if matrix[i][i] != 0:             
        is_ok = False
    for j in range(size):
        if matrix[i][j] != matrix[j][i]: 
            is_ok = False

print("YES" if is_ok else "NO")