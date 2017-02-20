class CheckBalanced {
	public static int checkHeight(Node root) {
		if (root == null) return -1;
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

	boolean isBalanced(Node root) {
		return checkHeight(root) != Integer.MIN_VALUE;
	}

	public static void main(String[] args) {
		
	}
}