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
        if self.head:
            d = {}
            d[self.head.data] = 1
            n = self.head
            prev = Node()
            while n:
                if n.data in d:
                    prev.next = n.next
                else:
                    d[n.data] = 1
                    prev = n
                n = n.next
    def printNodes(self):
        if self.head:
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
    print("\n")
    llist.deleteDups()
    llist.printNodes()
main()