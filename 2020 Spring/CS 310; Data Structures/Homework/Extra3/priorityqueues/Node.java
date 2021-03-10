package priorityqueues;

public class Node<E>{

	public int priority;
	public E data;
	public Node<E> nextNode;
	
	public Node(E i, int pr)
	{
		data=i;
		priority=pr;
		nextNode=null;
	}
}
