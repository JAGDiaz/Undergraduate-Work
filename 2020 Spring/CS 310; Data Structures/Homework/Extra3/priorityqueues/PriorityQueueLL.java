package priorityqueues;
import java.util.*;

/* This is an implementation of a sorted List.
 * insertItem() always inserts the element according to priority
 */

public class PriorityQueueLL<E> implements PriorityQueueInterface<E>{

	private Node<E> head;
	
	public PriorityQueueLL()
	{
		head=null;
	
	}
	
	public void insertItem(E element, int elementpr)
	{
		Node<E> temp,p;
		temp=new Node<E>(element,elementpr);
		
		if(isEmpty()||elementpr<head.priority)
		{
			temp.nextNode=head;
			head=temp;
		}
		else
		{
			p=head;
			while(p.nextNode!=null && p.nextNode.priority<=elementpr)
					p=p.nextNode;
			temp.nextNode=p.nextNode;
			p.nextNode=temp;
		}
	}
	
	public E removeMin()
	{
		E delData;
		if(isEmpty())
		{
			System.out.println("Queue Underflow");
			throw new NoSuchElementException();
		}
		else
		{
			delData=head.data;
			head=head.nextNode;
		}
		return delData;
	}
	
	public E minElement()
	{
		if(isEmpty())
		{
			System.out.println("Queue is Empty!!");
			throw new NoSuchElementException();
		}
		else
			return head.data;
	}
	
	public int minPriority()
	{
		if(isEmpty())
		{
			System.out.println("Queue is Empty!!");
			throw new NoSuchElementException();
		}
		else
			return head.priority;
	}
	
	public boolean isEmpty()
	{
		return (head==null);
	}
	
	public void display()
	{
		Node<E> p=head;
		if(isEmpty())
			System.out.println("Queue is Empty!");
		else
		{
			System.out.println("Queue is :");
			System.out.println("Element priority");
			while(p!=null)
			{
				System.out.println(p.data+" "+p.priority);
				p=p.nextNode;
			}
		}
		System.out.println("");
	}
	
}
