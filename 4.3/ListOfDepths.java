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

  public static ArrayList<LinkedList<TreeNode>> createLevelLinkedList(TreeNode root) {
    ArrayList<LinkedList<TreeNode>> lists = new ArrayList<LinkedList<TreeNode>>();
    createLevelLinkedList(root, lists, 0);
    return lists;
  }

  public static void main(String[] args) {
    int[] testArray = {2};
    TreeNode minBST = new TreeNode();
    minBST = minBST.createMinimalBST(testArray);
    ArrayList<LinkedList<TreeNode>> depthLists = createLevelLinkedList(minBST);
    System.out.println(depthLists.size());
  }
}
