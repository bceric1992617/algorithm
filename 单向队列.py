class queue:
    def __init__(self):
        self.list = []
    
    def push(self,item):
        self.list.append(item)

    def get(self):
        return self.list[0]

    def size(self):
        return len(self.list)

    def ergodic(self):
        for v in self.list:
            print(v)
        
    def search(self,item):
        isSet = False
        for v in self.list:
            if v == item:
                isSet = True
                break
        return isSet

    def removehHead(self): 
        if bool(self.list):
            self.list.pop(0)
            print('删除失败，列表是空')
        else:
            print('删除成功')
        
    def removeRear(self):
        if bool(self.list):
            self.list.pop()
            print('删除失败，列表是空')
        else:
            print('删除成功')

    def remove(self,item):
        self.list.remove(item)
    

if __name__ == '__main__':
    queue = queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.remove(2)
    queue.ergodic()

            