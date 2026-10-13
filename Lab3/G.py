class Stack():
    def __init__(self):
        self.items = []
        self.length = 0
        
    def is_empty(self):
        return self.items == [] 
    
    def push(self, item):
        self.items.append(item)
        self.length += 1
      
    def back(self):
        if self.is_empty():
            return
        return self.items[-1]
    
    def pop(self):
        if self.is_empty():
            return
        self.length -= 1    
        return self.items.pop()
    
    def solution(self):
        n = int(input())
        lst = list(map(int, input().split()))
        curr = 1
        for i in range(n):
            if lst[i] == curr:
                curr += 1
                continue
            while self.back() == curr:
                curr += 1
                self.pop()
            self.push(lst[i])
        while self.back() == curr:
            curr += 1
            self.pop()
        return 'YES' if self.length == 0 else 'NO'
        
s = Stack()
print(s.solution())
            