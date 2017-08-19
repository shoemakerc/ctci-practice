class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def appendToTail(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = newNode
    def deleteMid(self, badNode):
        newNext = badNode.next
        badNode.data = newNext.data
        badNode.next = badNode.next.next
    def deleteDups(self):
        if not self.head:
            return
        d = {}
        prev = Node()
        n = self.head
        while n:
            if n.data in d:
                prev.next = n.next
            else:
                d[n.data] = 1
                prev = n
            n = n.next
    def printNodes(self):
        if not self.head:
            return
        n = self.head
        while n:
            print(n.getData())
            n = n.next
    def partition(self, n):
        if not self.head or not self.head.next:
            return
        ptr1 = self.head
        ptr2 = self.head.next
        done = False
        while not done:
            while ptr1 and ptr1.data < n:
                ptr1 = ptr1.next
            while ptr2 and ptr2.data >= n:
                ptr2 = ptr2.next
            if not ptr1 or not ptr2:
                done = True
            else:
                ptr1.data, ptr2.data = ptr2.data, ptr1.data
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newData):
        self.data = newData
    def setNext(self, newNext):
        self.next = newNext

def main():
    llist = LinkedList(Node(5))
    llist.appendToTail(4)
    llist.appendToTail(4)
    llist.appendToTail(4)
    llist.appendToTail(1)
    llist.appendToTail(3)
    llist.appendToTail(3)
    llist.appendToTail(4)
    '''
    llist.appendToTail(4)
    llist.appendToTail(4)
    llist.appendToTail(4)
    llist.appendToTail(5)
    '''
    llist.printNodes()
    print("")
    llist.partition(3)
    llist.printNodes()
    print('')
    llist.deleteDups()
    llist.printNodes()
    print('')
    llist2 = LinkedList(Node(2))
    llist2.appendToTail(1)
    llist2.appendToTail(4)
    llist2.appendToTail(4)  
    print('')
    llist2.partition(3)
    llist2.printNodes()
main()