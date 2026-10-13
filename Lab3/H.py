from collections import deque
import sys
 

deq_lt = deque()
deq_rt = deque()
data = sys.stdin.read().split()
n = data[0]
index = 1

for i in range(int(n)):
    s = data[index]
    if s == '*':
        deq_rt.appendleft(int(data[index+1]))
        index += 2
    elif s == '+':
        deq_rt.append(int(data[index+1]))
        index += 2
    else:
        print(deq_lt.popleft())
        index += 1
    if len(deq_lt) < len(deq_rt):
        deq_lt.append(deq_rt.popleft())
    elif len(deq_lt) > len(deq_rt) + 1:
        deq_rt.appendleft(deq_lt.pop())
    