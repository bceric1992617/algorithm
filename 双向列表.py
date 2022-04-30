class node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.pre = None

class doubleLinkedList:
    def __init__(self):
        self._head = None

    def add(self,item):
        cur = self._head
        info = node(item)
        if cur == None:
            self._head = info
        else:
            cur.pre = info
            info.next = cur 
            self._head = info

    def append(self,item):
        cur = self._head
        if cur == None:
            self.add(item)
        else:
            while cur.next:
                cur = cur.next
            info = node(item)
            info.pre = cur
            cur.next = info

    def insert(self,item,num):
        cur = self._head
        if num <= 0:
            self.add(item)
        elif num > self.length():
            self.append(item)
        else:
            n = 0
            while cur.next:
                if n == (num - 1):
                    break
                cur = cur.next
                n += 1
            info = node(item)
            info.next = cur.next
            info.pre = cur
            cur.next = info

    def remove(self,item):
        cur = self._head
        while cur:
            if cur.item == item:
                break
            pre = cur
            cur = cur.next

        if cur == None:
            print('没有这个元素')
        else:
            pre.next = cur.next
            cur.pre = pre

    def search(self,item):
        cur = self._head
        isSet = False
        while cur:
            if cur.item == item:
                isSet = True
                break
            else:
                cur = cur.next
        return isSet
        

    def length(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def ergodic(self):
        cur = self._head
        if cur == None:
            print('None')
        else:
            while cur:
                print(cur.item)
                cur = cur.next

if __name__ == '__main__':
    doubleLinkedList = doubleLinkedList()
    doubleLinkedList.add(10)
    doubleLinkedList.add(20)
    doubleLinkedList.add(30)
    doubleLinkedList.add(40)
    # print(doubleLinkedList.search(110))
    # doubleLinkedList.ergodic()

            
        