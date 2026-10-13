class Stack():
    def __init__(self):
        self.items = []
        self.len = 0
        
    def is_empty(self):
        return self.items == [] 
    
    def push(self, item):
        self.items.append(item)
        self.len += 1
        print("ok")
    
    def size(self):
        print(self.len)
      
    def back(self):
        if self.is_empty():
            print("error")
            return
        print(self.items[-1])
    
    def pop(self):
        if self.is_empty():
            print("error")
            return
        self.len -= 1    
        print(self.items.pop())
    
    def clear(self):
        self.items = []
        self.len = 0
        print("ok")
        
s = Stack()
while True:
    oper= input().split()
    command = oper[0]
    if command == "push":
        n = int(oper[1])
        s.push(n)
    elif command == "pop":
        s.pop()
    elif command == "back":
        s.back()
    elif command == "size":
        s.size()
    elif command == "clear":
        s.clear()
    elif command == "exit":
        print("bye")
        break
    
            

    

    
        