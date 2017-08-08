from binary_tree import BinaryTree

def is_subtree(t1, t2):
    '''Algorithm to verify if BinaryTree t2 is a subtree of (larger) BinaryTree t1'''
    if !t2:
        if t1:
            return False
        else:
            return True
    else:
        if t2.key == t1.key:
            is_subtree(t1.left, t2.left)
            is_subtree(t1.right, t2.right)
