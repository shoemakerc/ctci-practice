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

  // Method to print out nodes in BST in order
  public static void inOrderTraversal(TreeNode node) {
    if (node != null) {
      inOrderTraversal(node.left);
      System.out.print(node.value + ", ");
      inOrderTraversal(node.right);
    }
  }
}

class MinimalTree {
  public static void main(String[] args) {
    int[] testArray = {1, 2, 3, 4, 5, 6, 7, 8};
    TreeNode minBST = new TreeNode();
    minBST = minBST.createMinimalBST(testArray);
    System.out.print("[");
    TreeNode.inOrderTraversal(minBST);
    // Delete extraneous whitespace and comma
    System.out.print("\b\b]");
  }
}
