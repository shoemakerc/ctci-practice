/*
BinaryTree.java
Base class for implementing a binary tree
*/

class BinaryTree {
	private Node root;
	
	private static class Node {
		Node left;
		Node right;
		int data;

		Node(int n) {
			left = null;
			right = null;
			data = n;
		}
	}

	public void BinaryTree() {
		root = null;
	}

	public boolean lookup(int data) {
		return lookup(root, data);
	}

	public boolean lookup(Node node, int data) {
		if (node == null) {
			return false;
		}
		if (data == node.data) {
			return true;
		} else if (data < node.data) {
			return lookup(node.left, data);
		} else {
			return lookup(node.right, data);
		}
	}

	public void insert(int data) {
		root = insert(root, data);
	}

	public static Node insert(Node node, int data) {
		if (node == null) {
			node = new Node(data);
		} else {
			if (data <= node.data) {
				node.left = insert(node.left, data);
			} else {
				node.right = insert(node.right, data);
			}
		}
		return node;
	}

	// Begin 4.4
	public static int checkHeight(Node root) {
		if (root == null) {
			return -1;
		}

		int leftHeight = checkHeight(root.left);
		if (leftHeight == Integer.MIN_VALUE) {
			return Integer.MIN_VALUE;
		}

		int rightHeight = checkHeight(root.right);
		if (rightHeight == Integer.MIN_VALUE) {
			return Integer.MIN_VALUE;
		}

		int heightDiff = leftHeight - rightHeight;
		if (Math.abs(heightDiff) > 1) {
			return Integer.MIN_VALUE;
		} else {
			return Math.max(leftHeight, rightHeight) + 1;
		}
	}

	boolean isBalanced(Node root) {
		return checkHeight(root) != Integer.MIN_VALUE;
	}
	// End 4.4

	public static void main(String[] args) {
		BinaryTree tree = new BinaryTree();
		tree.insert(3);
		tree.insert(4);
		tree.insert(5);
		tree.insert(2);
		System.out.println(tree.isBalanced(tree.root));
	}
}