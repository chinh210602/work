class Stack():
    def __init__(self):
        self.stack = []
        self.max = -10000
        self.max_cache = []
        
    def push(self, x):
        self.stack.append(x)
        if x > self.max:
            self.max = x
            self.max_cache.append(x)
            
    def pop(self):
        x = self.stack.pop()
        if x == self.max:
            self.max_cache.pop()
            self.max = self.max_cache[-1]
            
    def Max(self):
        return self.max
    
if __name__ == "__main__":
    n = int(input())
    stack = Stack()
    result = []
    for _ in range(n):
        input_ = input().split()
        if len(input_) == 2:
            query, number = input_[0], int(input_[1])
            stack.push(number)
        if input_[0] == "max": result.append(stack.Max())
        elif input_[0] == "pop": stack.pop()
    
    for i in result:
        print(i)