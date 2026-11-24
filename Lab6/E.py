import sys

def main():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    m = int(numbers[1])

    neighbors = [[] for _ in range(n + 1)]      
    for i in range(m):
        a = int(numbers[2 + 2 * i])
        b = int(numbers[3 + 2 * i])
        neighbors[a].append(b)
        neighbors[b].append(a)          

    visited = [False] * (n + 1)
    components = []                     

    for start in range(1, n):
        if visited[start]:
            continue                    

        visited[start] = True
        stack = [start]
        component = []

        while stack:
            current = stack.pop()
            component.append(current)
            for neighbor in neighbors[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        component.sort()               
        components.append(component)

    result = [str(len(components))]
    for component in components:
        result.append(str(len(component)))
        result.append(" ".join(map(str, component)))
    print("\n".join(result))

main()