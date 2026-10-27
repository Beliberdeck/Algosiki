import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    ev = []
    for i in range(n):
        t = int(data[1 + 2 * i]); l = int(data[2 + 2 * i])
        ev.append((t, 1))        # начало
        ev.append((t + l, 0))    # конец (на тот же момент обрабатывается раньше начала)
    ev.sort()
    cur = best = 0
    for _, typ in ev:
        if typ:
            cur += 1
            best = max(best, cur)
        else:
            cur -= 1
    print(best)

main()
