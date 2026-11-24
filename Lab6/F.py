import sys

numbers = sys.stdin.read().split()
n = int(numbers[0])

matrix = []
for row_index in range(n):
    begin = 1 + row_index * n
    matrix.append(list(map(int, numbers[begin:begin + n])))

vhodnaya_stepen = [0] * n
for source in range(n):
    for target in range(n):
        vhodnaya_stepen[target] += matrix[source][target]

svobodnye = []                      
for vertex in range(n):
    if vhodnaya_stepen[vertex] == 0:
        svobodnye.append(vertex)

removed = 0
while svobodnye:
    current = svobodnye.pop()
    removed += 1
    for target in range(n):
        if matrix[current][target] == 1:
            vhodnaya_stepen[target] -= 1        
            if vhodnaya_stepen[target] == 0:
                svobodnye.append(target)        

print(0 if removed == n else 1)