class Stack():
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, x):
        self.items.append(x)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.items.pop()
    
    def back(self):
        return self.items[-1]
    
    def solution(self):
        st = input().split()
        for el in st:
            if el == '*':
                self.push(self.pop() * self.pop())
            elif el == '+':
                self.push(self.pop() + self.pop())
            elif el == '-':
                self.push(-1*(self.pop() - self.pop()))
            else:
                self.push(int(el))
        return self.back()
    
s = Stack()
print(s.solution())
