/*
ListOfDepths.java
Problem #4.3
From Cracking the Code Interview, 6th Edition

Given a sorted increasing-order array turned into a BST of minimal height, creates a linked list of all 
the nodes in the BST at each depth (i.e. for a tree with depth D, we will have a list of D linked lists)
*/


import java.util.ArrayList;
import java.util.LinkedList;

class TreeNode {
	public int value;
	public TreeNode left;
	public TreeNode right;

	public TreeNode() {

	}

	public TreeNode(int n) {
		value = n;
	}

	public static TreeNode createMinimalBST(int array[]) {
		return createMinimalBST(array, 0, array.length - 1);
	}

	public static TreeNode createMinimalBST(int arr[], int start, int end) {
		if (end < start) {
			return null;
		}
		int mid = (start + end) / 2;
		TreeNode n = new TreeNode(arr[mid]);
		n.left = createMinimalBST(arr, start, mid - 1);
		n.right = createMinimalBST(arr, mid + 1, end);
		return n;
	}
}

class ListOfDepths {

	public static ArrayList<LinkedList<TreeNode>> createLevelLinkedList(TreeNode root) {
		ArrayList<LinkedList<TreeNode>> listOfLevels = new ArrayList<LinkedList<TreeNode>>();
		createLevelLinkedList(root, listOfLevels, 0);
		return listOfLevels;
	}

	public static void createLevelLinkedList(TreeNode root, ArrayList<LinkedList<TreeNode>> lists, int level) {
		if (root == null) return; // base case

		LinkedList<TreeNode> list = null;
		if (lists.size() == level) { // Level not contained in lists
			list = new LinkedList<TreeNode>();
			lists.add(list);
		} else {
			list = lists.get(level);
		}
		list.add(root);
		createLevelLinkedList(root.left, lists, level + 1);
		createLevelLinkedList(root.right, lists, level + 1);
	}

	public static void main(String[] args) {
		int[] testArray = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		TreeNode minBST = new TreeNode();
		minBST = minBST.createMinimalBST(testArray);

		ArrayList<LinkedList<TreeNode>> depthLists = createLevelLinkedList(minBST);

		// Verify by displaying all LinkedLists in depthLists
		System.out.println(depthLists.size());
		for (int i = 0; i < depthLists.size(); i++) {
			TreeNode[] nodes = depthLists.get(i).toArray(new TreeNode[0]);
			System.out.print("Level " + (i + 1) + ": [");
			for (int j = 0; j < nodes.length; j++) {
				if (j < nodes.length - 1) {
					System.out.print(nodes[j].value + ", ");
				} else {
					System.out.print(nodes[j].value);
				}
			}
			System.out.print("]\n");
		}
	}
}
