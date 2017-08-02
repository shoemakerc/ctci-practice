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

	// Begin 4.5
	boolean checkBST(Node n) {
		return checkBST(n, null, null);
	}

	boolean checkBST(Node n, Integer min, Integer max) {
		if (n == null) {
			return true;
		}

		if ((min != null && n.data <= min) || (max != null && n.data > max)) {
			return false;
		}

		if (!checkBST(n.left, min, n.data) || !checkBST(n.right, n.data, max)) {
			return false;
		}

		return true;
	}
	// End 4.5

	public static void main(String[] args) {
		BinaryTree tree = new BinaryTree();
		tree.insert(3);
		tree.insert(4);
		tree.insert(5);
		tree.insert(2);
		tree.insert(1);
		tree.insert(1);
		System.out.println(tree.checkBST(tree.root));
	}
}