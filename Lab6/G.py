import sys

numbers = sys.stdin.read().split()
n = int(numbers[0])
m = int(numbers[1])


lider = list(range(n + 1))

def find_lider(vertex):
    while lider[vertex] != vertex:
        lider[vertex] = lider[lider[vertex]]
        vertex = lider[vertex]
    return vertex

groups = n
for i in range(m):
    a = int(numbers[2 + 2 * i])
    b = int(numbers[3 + 2 * i])
    lider_a = find_lider(a)
    lider_b = find_lider(b)
    if lider_a != lider_b:
        lider[lider_a] = lider_b        
        groups -= 1

is_tree = (m == n - 1) and (groups == 1)
print("YES" if is_tree else "NO")