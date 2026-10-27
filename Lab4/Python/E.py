import sys
import heapq

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    h = list(map(int, data[1:1 + n]))
    heapq.heapify(h)
    total = 0
    while len(h) > 1:
        s = heapq.heappop(h) + heapq.heappop(h)
        total += s
        heapq.heappush(h, s)
    print("%d.%02d" % (total // 20, (total % 20) * 5))

main()
