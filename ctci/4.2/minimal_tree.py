class Node:
    def __init__(self, nodeVal):
        self.key = nodeVal
        self.left = None
        self.right = None

    def getRoot(self):
        return self.key

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

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

def arr_to_BST(arr):
    return arr_to_BST_helper(arr, 0, len(arr) - 1)
def arr_to_BST_helper(arr, lo, hi):
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    newNode = Node(arr[mid])
    print(newNode.key)
    newNode.left = arr_to_BST_helper(arr, lo, mid - 1)
    newNode.right = arr_to_BST_helper(arr, mid + 1, hi)
    return newNode
def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    root = arr_to_BST(lst)
    preorder(root)
main()