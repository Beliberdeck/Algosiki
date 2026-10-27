import sys
import heapq

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    size = [int(x) for x in data[1:1 + n]]
    h = [(max(1000 - size[i], 1), i) for i in range(n)]
    heapq.heapify(h)
    pos, tm = 0, 0
    while True:
        t, i = heapq.heappop(h)
        if abs(i - pos) > t - tm:
            print(t)
            return
        pos, tm = i, t
        size[i] += 1
        heapq.heappush(h, (t + max(1000 - size[i], 1), i))

main()
