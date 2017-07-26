class Node {
	private int data;
	protected Node next;
	public Node(int data, Node next) {
		this.data = data;
		this.next = next;
	}
	public void printNode() {
		if (this.next != null) {
			System.out.print(this.data + ", ");
		} else {
			System.out.print(this.data + "]");
		}
	}
}

class myLinkedList {
	private Node head;

	public myLinkedList() {
		head = null;
	}
	public boolean isEmpty() {
		return head == null;
	}
	public void insert(int i) {
		Node newNode = new Node(i, head);
		head = newNode;
	}
	public void deleteFromFront() {
		Node curr = head;
		head = curr.next;
		head.next = curr.next.next;
	}
	public void printList() {
		Node curr = head;
		System.out.print("Linked list: [");
		while (curr != null) {
			curr.printNode();
			curr = curr.next;
		}
		System.out.print("\n");
	}
}

class LinkedListTest {
	public static void main(String[] args) {
		myLinkedList list = new myLinkedList();
		list.insert(3);
		list.insert(51);
		list.insert(3);
		list.insert(4);
		list.printList();
		list.deleteFromFront();
		list.printList();
		list.deleteFromFront();
		list.printList();
	}
}
