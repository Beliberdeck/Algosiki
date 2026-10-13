class Deque():
    def __init__(self):
        self.items = []
        self.length = 0
        
    def push_front(self, x):
        self.length += 1
        self.items = [x] + self.items
        print('ok')
        
    def push_back(self, x):
        self.length += 1
        self.items.append(x)
        print("ok")
        
    def pop_front(self):
        if self.length == 0:
            print('error')
            return
        self.length -= 1
        print(self.items.pop(0))
        
    def pop_back(self):
        if self.length == 0:
            print('error')
            return
        self.length -= 1
        print(self.items.pop())
        
    def front(self):
        if self.length == 0:
            print('error')
            return
        print(self.items[0])
        
    def back(self):
        if self.length == 0:
            print('error')
            return
        print(self.items[-1])
        
    def size(self):
        print(self.length)
        
    def clear(self):
        self.length = 0
        self.items = []
        print('ok')
        
    def solution(self):
        while True:
            st = input().split()
            if st[0] == 'push_back':
                self.push_back(int(st[1]))
            elif st[0] == 'push_front':
                self.push_front(int(st[1]))     
            elif st[0] == 'pop_back':
                self.pop_back()
            elif st[0] == 'pop_front':
                self.pop_front()
            elif st[0] == 'front':
                self.front()
            elif st[0] == 'size':
                self.size()
            elif st[0] == 'back':
                self.back()
            elif st[0] == 'clear':
                self.clear()
            else:
                print('bye')
                break
s = Deque()
s.solution()