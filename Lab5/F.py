import sys


def read_seq():
    res = []
    for t in sys.stdin.read().split():
        v = int(t)
        if v == 0:
            break
        res.append(v)
    return res


def build(seq):
    # дерево храним в масивах, L и R это номера детей (-1 если ребенка нет)
    val, L, R, cnt = [], [], [], []
    for x in seq:
        if not val:
            val.append(x); L.append(-1); R.append(-1); cnt.append(1)
            continue
        cur = 0
        while True:
            if x == val[cur]:
                cnt[cur] += 1
                break
            nxt = L[cur] if x < val[cur] else R[cur]
            if nxt == -1:
                val.append(x); L.append(-1); R.append(-1); cnt.append(1)
                if x < val[cur]:
                    L[cur] = len(val) - 1
                else:
                    R[cur] = len(val) - 1
                break
            cur = nxt
    return val, L, R, cnt


def inorder(L, R):
    # обход без рекурсии
    res, st = [], []
    cur = 0 if L else -1
    while st or cur != -1:
        while cur != -1:
            st.append(cur)
            cur = L[cur]
        cur = st.pop()
        res.append(cur)
        cur = R[cur]
    return res


def bfs(L, R):
    # обход в ширину
    order = [0] if L else []
    for u in order:
        if L[u] != -1: order.append(L[u])
        if R[u] != -1: order.append(R[u])
    return order


val, L, R, cnt = build(read_seq())
print("\n".join(str(val[u]) for u in inorder(L, R) if L[u] == -1 and R[u] == -1))
