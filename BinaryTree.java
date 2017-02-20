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

	public Node insert(Node node, int data) {
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
}