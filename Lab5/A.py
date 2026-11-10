import sys


class Node:
    __slots__ = ("v", "l", "r")

    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None


root = None


def search(x):
    cur = root
    while cur and cur.v != x:
        cur = cur.l if x < cur.v else cur.r
    return cur is not None


def add(x):
    global root
    if root is None:
        root = Node(x)
        return True
    cur = root
    while True:
        if x == cur.v:
            return False
        if x < cur.v:
            if cur.l is None:
                cur.l = Node(x)
                return True
            cur = cur.l
        else:
            if cur.r is None:
                cur.r = Node(x)
                return True
            cur = cur.r


def delete(x):
    global root
    parent, cur = None, root
    while cur and cur.v != x:
        parent = cur
        cur = cur.l if x < cur.v else cur.r
    if cur is None:
        return False
    # если у вершины два сына то меняем значение с макс. слева и удаляем уже его
    if cur.l and cur.r:
        # меняем значение с максимумом левого поддерева и удаляем этот максимум
        pp, m = cur, cur.l
        while m.r:
            pp, m = m, m.r
        cur.v = m.v
        parent, cur = pp, m
    # теперь у cur максимум один ребенок подвязываем его к родителю
    child = cur.l if cur.l else cur.r
    if parent is None:
        root = child
    elif parent.l is cur:
        parent.l = child
    else:
        parent.r = child
    return True


def print_tree(out):
    # тоже без рекурсии левое, потом сам узел с точками, потом правое
    # обход left, текущий, right
    st = []
    cur, level = root, 0
    levels = []
    while st or cur:
        while cur:
            st.append((cur, level))
            cur = cur.l
            level += 1
        cur, level = st.pop()
        out.append("." * level + str(cur.v))
        cur = cur.r
        level += 1


out = []
for line in sys.stdin.read().split("\n"):
    p = line.split()
    if not p:
        continue
    c = p[0]
    if c == "ADD":
        out.append("DONE" if add(int(p[1])) else "ALREADY")
    elif c == "DELETE":
        out.append("DONE" if delete(int(p[1])) else "CANNOT")
    elif c == "SEARCH":
        out.append("YES" if search(int(p[1])) else "NO")
    elif c == "PRINTTREE":
        print_tree(out)
print("\n".join(out))
