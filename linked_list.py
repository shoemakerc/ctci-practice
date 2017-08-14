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
        n = self.head
        d[n.data] = 1
        n = n.next
        prev = Node()
        while n:
            if n.data in d:
                print("Removing", n.data)
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
    llist = LinkedList(Node(2))
    llist.appendToTail(2)
    llist.appendToTail(3)
    llist.appendToTail(4)
    llist.appendToTail(1)
    llist.appendToTail(6)
    llist.appendToTail(2)
    llist.appendToTail(1)
    llist.appendToTail(9)
    llist.appendToTail(1)
    llist.appendToTail(9)
    llist.appendToTail(9)
    llist.appendToTail(9)
    llist.appendToTail(9)
    llist.printNodes()
    print("")
    llist.deleteDups()
    ar = []
    while llist:
        ar.append(llist.head.getData())
        llist.head = llist.head.next
main()