class Queue():
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, x):
        self.length += 1
        self.items.append(x)
        print('ok')

    def pop(self):
        if self.length == 0:
            print('error')
            return
        self.length -= 1
        print(self.items.pop(0))

    def front(self):
        if self.length == 0:
            print('error')
            return
        print(self.items[0])

    def size(self):
        print(self.length)

    def clear(self):
        self.items = []
        self.length = 0
        print('ok')

    def solution(self):
        while True:
            st = input().split()
            if st[0] == 'push':
                self.push(int(st[1]))
            elif st[0] == 'pop':
                self.pop()
            elif st[0] == 'front':
                self.front()
            elif st[0] == 'size':
                self.size()
            elif st[0] == 'clear':
                self.clear()
            else:
                print('bye')
                break

s = Queue()
s.solution()
    
    