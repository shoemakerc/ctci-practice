# Class definition of a typical binary tree
class BinaryTree:
    def __init__(self, rootVal):
        self.key = rootVal
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.right = self.right
            self.right = temp

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRoot(self, val):
        self.key = val

    def getRoot(self):
        return self.key

# traversals
def preorder(tree):
    if tree:
        print(tree.getRoot(), end = " ")
        preorder(tree.getLeft())
        preorder(tree.getRight())
def inorder(tree):
    if tree:
        preorder(tree.getLeft())
        print(tree.getRoot(), end = " ")
        preorder(tree.getRight())
def postorder(tree):
    if tree:
        preorder(tree.getLeft())
        preorder(tree.getRight())
        print(tree.getRoot(), end = " ")

def main():
    # Demonstration code for BinaryTree class
    tree = BinaryTree('b')
    print(tree.key)
    print(tree.getLeft()) # prints None
    tree.insertLeft('a')
    print(tree.getLeft()) # returns object (BinaryTree) instance
    tree.insertRight('c')
    print(tree.getLeft().key) # returns key value
    print(tree.getRight().key)
    print(tree.getLeft().getRoot()) # also returns key value
    preorder(tree)
    print("\n")
    inorder(tree)
    print("\n")
    postorder(tree)
main()