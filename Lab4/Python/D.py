import sys
import heapq

def main():
    h = []
    out = []
    data = sys.stdin.read().split()
    i = 0
    while i < len(data):
        c = data[i]
        if c == 'CLEAR':
            h = []
            i += 1
        elif c == 'ADD':
            heapq.heappush(h, -int(data[i + 1]))
            i += 2
        else:  
            out.append(str(-heapq.heappop(h)) if h else 'CANNOT')
            i += 1
    print('\n'.join(out))

main()
