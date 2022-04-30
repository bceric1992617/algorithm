class stack:
    def __init__(self):
        self.list = [] 
    
    def push(self,item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]

    def ergodic(self):
        list = self.list
        list.reverse()
        for v in list:
            print(v)
    
    def size(self):
        return len(self.list)
    
if __name__ == '__main__':
    stack = stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.size())
    stack.ergodic()
