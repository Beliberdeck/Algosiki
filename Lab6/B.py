import sys

numbers = sys.stdin.read().split()
size = int(numbers[0])

matrix = []
for row_index in range(size):
    begin = 1 + row_index * size
    matrix.append(list(map(int, numbers[begin:begin + size])))

istoki = []     
stoki = []      

for vertex in range(size):
    has_incoming = False
    for other in range(size):
        if matrix[other][vertex] == 1:
            has_incoming = True

    has_outgoing = False
    for other in range(size):
        if matrix[vertex][other] == 1:
            has_outgoing = True

    if not has_incoming:
        istoki.append(vertex + 1)
    if not has_outgoing:
        stoki.append(vertex + 1)

print(len(istoki))
for vertex in istoki:
    print(vertex)
print(len(stoki))
for vertex in stoki:
    print(vertex)