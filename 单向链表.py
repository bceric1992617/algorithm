class node:
    def __init__(self,item):
        self.item = item
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self._head = None

    def singlyLinkedAdd(self,item):
        info = node(item)
        info.next = self._head
        self._head = info


    def singlyLinkedAppend(self,item):
        info = node(item)
        cur = self._head
        if cur == None:
            self.singlyLinkedAdd(item)
        else:
            while cur.next:
                cur = cur.next
            cur.next = info

    def singlyLinkedErgodic(self):
        cur = self._head
        if not cur:
            print('None')
        else:
            while cur.next:
                print(cur.item)
                cur = cur.next
            print(cur.item)

    def singlyLinkedLength(self):
        cur = self._head
        count = 0
        if cur == None:
            return count
        else:
            while cur.next:
                count += 1
                cur = cur.next
            return count+1

    def singlyLinkedInsert(self,item,num):
        cur = self._head
        if cur == None:
            self.add(item)
        else:
            if num <= 0:
                self.singlyLinkedAdd(item)
            elif num > self.singlyLinkedLength():
                self.singlyLinkedAppend(item)
            else:
                n = 0
                while cur.next:
                    if n == (num - 1):
                        break   
                    cur = cur.next
                    n += 1
                info = node(item)
                info.next = cur.next
                cur.next = info

    def isEmpty(self):
        cur = self._head
        return cur == None

    def singlyLinkedRemove(self,item):
        cur = self._head
        if cur == None:
            print('None')
        else:
            if item == cur.item:
                self._head = cur.next
            else:
                while cur.next:
                    pre = cur
                    cur = cur.next
                    if item == cur.item:
                        pre.next = cur.next
                        break
    
    def singlyLinkedSeach(self,item):
        cur = self._head
        isSet = False
        while cur:
            if cur.item == item:
                isSet = True
                break
            else:
                cur = cur.next
        return isSet

            
            

    

if __name__ == '__main__':
    singlyLinkedList = singlyLinkedList()
    singlyLinkedList.singlyLinkedAdd(99)
    singlyLinkedList.singlyLinkedAdd(98)
    singlyLinkedList.singlyLinkedAdd(96)
    print(singlyLinkedList.singlyLinkedSeach(11))



    

