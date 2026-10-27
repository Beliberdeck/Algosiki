import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    h = [0]
    out = []
    pos = 1
    for _ in range(n):
        cmd = data[pos]; pos += 1
        if cmd == '0':
            k = int(data[pos]); pos += 1
            h.append(k)
            i = len(h) - 1
            while i > 1 and h[i >> 1] < h[i]:
                h[i >> 1], h[i] = h[i], h[i >> 1]
                i >>= 1
        else:
            out.append(h[1])
            last = h.pop()
            size = len(h) - 1
            if size >= 1:
                h[1] = last
                i = 1
                while True:
                    l = i * 2
                    if l > size:
                        break
                    if l + 1 <= size and h[l + 1] > h[l]:
                        l += 1
                    if h[l] > h[i]:
                        h[l], h[i] = h[i], h[l]
                        i = l
                    else:
                        break
    print('\n'.join(map(str, out)))

main()

