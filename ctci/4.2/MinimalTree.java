/*
MinimalTree.java
Problem #4.2
From Cracking the Code Interview, 6th Edition

Given a sorted increasing-order array with unique integer elements, creates a BST of minimal height
*/

class TreeNode {
  public int value;
  public TreeNode left;
  public TreeNode right;

  public TreeNode() {

  }

  public TreeNode(int n) {
    this.value = n;
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

  public static void inOrderTraversal(TreeNode node) {
    if (node != null) {
      inOrderTraversal(node.left);
      System.out.print(node.value + ", ");
      inOrderTraversal(node.right);
    }
  }

  public static void preOrderTraversal(TreeNode node) {
    if (node != null) {
      System.out.print(node.value + ", ");
      preOrderTraversal(node.left);
      preOrderTraversal(node.right);
    }
  }

    public static void postOrderTraversal(TreeNode node) {
    if (node != null) {
      postOrderTraversal(node.left);
      postOrderTraversal(node.right);
      System.out.print(node.value + ", ");
    }
  }
}

class MinimalTree {
  public static void main(String[] args) {
    int[] testArray = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    TreeNode minBST = new TreeNode();
    minBST = minBST.createMinimalBST(testArray);

    // Testing w/ in-order traversal
    System.out.print("In-order traversal: [");
    TreeNode.inOrderTraversal(minBST);
    // Delete extraneous whitespace and comma
    System.out.print("\b\b]\n");

    // Testing w/ pre-order traversal
    System.out.print("Pre-order traversal: [");
    TreeNode.preOrderTraversal(minBST);
    // Delete extraneous whitespace and comma
    System.out.print("\b\b]\n");

    // Testing w/ post-order traversal
    System.out.print("Post-order traversal: [");
    TreeNode.postOrderTraversal(minBST);
    // Delete extraneous whitespace and comma
    System.out.print("\b\b]\n");
  }
}
