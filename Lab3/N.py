from collections import deque

first = deque(map(int, input().split()))
second = deque(map(int, input().split()))

moves = 0

while first and second:
    a = first.popleft()
    b = second.popleft()
    moves += 1

    if a == 0 and b == 9:
        first_wins = True
    elif a == 9 and b == 0:
        first_wins = False
    else:
        first_wins = a > b

    if first_wins:
        first.append(a)
        first.append(b)
    else:
        second.append(a)
        second.append(b)

if not first:
    print("second", moves)
elif not second:
    print("first", moves)
else:
    print("botva")