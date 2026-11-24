import sys

def main():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    m = int(numbers[1])

    edges_part = numbers[2:2 + 2 * m]
    permutation = numbers[2 + 2 * m:2 + 2 * m + n]

    position = [0] * (n + 1)
    for index, vertex in enumerate(permutation):
        position[int(vertex)] = index

    for i in range(m):
        from_vertex = int(edges_part[2 * i])
        to_vertex = int(edges_part[2 * i + 1])
        if position[from_vertex] >= position[to_vertex]:
            print("NO")
            return

    print("YES")

main()