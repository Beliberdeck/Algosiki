def anargram(a, b):
    if len(a) != len(b):
        return "NO"
    count = {}
    for x in a:
        count[x] = count.get(x, 0) + 1
    for x in b:
        if x not in count or count[x] == 0:
            return "NO"
        count[x] -= 1
    return "YES"

a = input()
b = input()
print(anargram(a, b))
