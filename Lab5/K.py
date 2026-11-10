import sys
from bisect import bisect_left, insort

MOD = 10 ** 9
MAXB = 1000  # максимальный размер блока

data = sys.stdin.buffer.read().split()
n = int(data[0])

# список блоков, внутри каждого числа отсортированы (так быстрее чем одно дерево)
buckets = []   # отсортированные блоки
maxes = []     # максимум каждого блока


def add(x):
    if not buckets:
        buckets.append([x])
        maxes.append(x)
        return
    i = bisect_left(maxes, x)
    if i == len(buckets):
        i -= 1
    b = buckets[i]
    j = bisect_left(b, x)
    if j < len(b) and b[j] == x:
        return
    b.insert(j, x)
    maxes[i] = b[-1]
    # блок стал слишком большой - пополам
    if len(b) > MAXB:
        half = len(b) // 2
        nb = b[half:]
        del b[half:]
        buckets.insert(i + 1, nb)
        maxes[i] = b[-1]
        maxes.insert(i + 1, nb[-1])


def nxt(x):
    i = bisect_left(maxes, x)
    if i == len(buckets):
        return -1
    b = buckets[i]
    return b[bisect_left(b, x)]


out = []
y = 0
# last_query - надо ли прибавлять y к числу
last_query = False
pos = 1
for _ in range(n):
    op = data[pos]
    v = int(data[pos + 1])
    pos += 2
    if op == b"+":
        add((v + y) % MOD if last_query else v)
        last_query = False
    else:
        y = nxt(v)
        out.append(y)
        last_query = True
print("\n".join(map(str, out)))
