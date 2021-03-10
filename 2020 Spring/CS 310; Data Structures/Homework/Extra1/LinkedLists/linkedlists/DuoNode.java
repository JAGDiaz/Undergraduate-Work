package linkedlists;

public class DuoNode<E> 
{

	public E data;
	public DuoNode<E> nextNode;
	public DuoNode<E> prevNode;
	
	public DuoNode(E data)
	{
		this(data,null, null);
	}
	

	public DuoNode(E data, DuoNode<E> next, DuoNode<E> prev)
	{
		this.data = data;
		this.nextNode = next;
		this.prevNode = prev;
	}
	public void printInfo()
	{
		System.out.println("The previous node contains: " + this.prevNode.data);
		System.out.println("This node contains: " + this.data);
		System.out.println("The next node contains: " + this.nextNode.data);
	}
	
}
