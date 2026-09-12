def compare(a, b):
    return a + b > b + a


pieces = []
while True:
    try:
        pieces.append(input())
    except EOFError:
        break
      
for i in range(1, len(pieces)):
    current = pieces[i]
    j = i - 1
    while j >= 0 and not compare(pieces[j], current):
        pieces[j + 1] = pieces[j]
        j -= 1
    pieces[j + 1] = current
print("".join(pieces))
