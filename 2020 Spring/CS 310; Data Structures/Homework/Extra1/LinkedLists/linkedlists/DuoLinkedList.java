package linkedlists;

public class DuoLinkedList<E> 
{
	private DuoNode<E> head = null;
	
	/* Inserts*/
	public void insertAtHead(E data)
	{
		if(this.head == null)
		{
			this.head = new DuoNode<E>(data);
			this.head.nextNode = this.head;
			this.head.prevNode = this.head;
		}
		else if(this.length == 1)
		{
			DuoNode<E> temp = new DuoNode<E>(data);
			temp.nextNode = this.head;
			this.head.prevNode = temp;
			temp.prevNode = this.head;
			this.head.nextNode = temp;
			this.head = temp;
		}
		else
		{
			DuoNode<E> temp = new DuoNode<E>(data);
			temp.nextNode = this.head;
			temp.prevNode = this.head.prevNode; 
			temp.prevNode.nextNode = temp;
			this.head.prevNode = temp;
			this.head = temp;
		}
	}
	public void insertAtEnd(E data)
	{
		if(this.head == null)
		{
			this.head = new DuoNode<E>(data);
			this.head.nextNode = this.head;
			this.head.prevNode = this.head;
		}
		else
		{
			DuoNode<E> newDuoNode = new DuoNode<E>(data);
			newDuoNode.nextNode = this.head;
			newDuoNode.prevNode = this.head.prevNode;
			this.head.prevNode = newDuoNode;
			this.head.prevNode.prevNode.nextNode = this.head.prevNode;
			this.head.prevNode.nextNode.prevNode = this.findLast();

		}
	}
	public void insertAtPosition(E data, int position)
	{
		DuoNode<E> newDuoNode=new DuoNode<E>(data);
		DuoNode<E> position_node = this.findAtPosition(position-1);
		if(position_node!=null)
		{
			newDuoNode.nextDuoNode=position_node.nextDuoNode;
			position_node.nextDuoNode=newDuoNode;
		}
	}
	
	/*Delete*/
	public DuoNode<E> deleteAtStart() 
	{
		DuoNode<E> toDel = this.head;
		this.head = this.head.nextDuoNode;
		return toDel;
	}
	public DuoNode<E> deleteAtEnd() 
	{
		DuoNode<E> toDel = this.findLast();
		this.findSecondLast().nextDuoNode=null;
		return toDel;
	}
	public DuoNode<E> deleteAtPosition(int position)
	{
		DuoNode<E> position_node = this.findAtPosition(position);
		DuoNode<E> prev_node=this.findAtPosition(position-1);
		prev_node.nextDuoNode=position_node.nextDuoNode;
		return position_node;
	}
	
	/* Search */
	public DuoNode<E> findWithData(E data) 
	{
		DuoNode<E> curr = this.head;
		do
		{
			if (curr.data==data) 
				return curr;
			curr = curr.nextDuoNode;
		}
		while (curr != this.head); 

		return null;
	}
	public DuoNode<E> searchNode(E data)
	{
		if(data == null || this.length() == 0)
			return null;
		
		DuoNode<E> curr = this.head;
		do
		{
			if(curr.data == data)
				return curr;
			curr= curr.nextDuoNode;
		}
		while(curr!=this.head);

		return null;
	}
	public DuoNode<E> findAtPosition(int position)
	{
		DuoNode<E> curr=this.head;
		int i = 1;
		do
		{
			curr=curr.nextDuoNode;
		}
		while(i++ < position && curr!=this.head);
		return curr;
	}
	
	/* Finding references*/
	public DuoNode<E> predWithData(E data)
	{
		DuoNode<E> curr = this.head;
		do
		{
			if(curr.nextDuoNode.data==data)
				return curr;
	
			curr=curr.nextDuoNode;
		}
		while (curr.nextDuoNode != this.head);
		return null;	
	}
	public DuoNode<E> findLast()
	{
		DuoNode<E> last_reference = this.head;
		do
			last_reference=last_reference.nextDuoNode;
		while(last_reference.nextDuoNode != this.head);
		return last_reference;
	}
	public DuoNode<E> findSecondLast()
	{
		DuoNode<E> second_last = this.head;
		do
			second_last=second_last.nextDuoNode;
		while((second_last.nextDuoNode.nextDuoNode) != this.head);
		return second_last;		
	}
	
	/*Length of the linked List*/
	public int length()
	 {
		if (head == null)
			return 0;
		int length = 0;
		DuoNode<E> curr = this.head;
		do
		{
			length += 1;
			curr = curr.nextDuoNode;
		}
		while (curr != this.head);
		return length;
	}
	public int recurseLength(DuoNode<E> next)
	{
		if(next == null)
			return 0;

		if(next.nextNode == this.head)
			return 1;
		else
			return recurseLength(next.nextNode) + 1;
	}
	
	/*Display - two ways*/
	public void displayList()
	{
		DuoNode<E> curr = this.head;
		System.out.print("\n{");
		do
		{
			System.out.print("Data:"+curr.data+" ");
			curr=curr.nextDuoNode;
		}
		while(curr!=this.head);
		System.out.print("}");
		System.out.println();
	
	}
	public String toString()
	{
		DuoNode<E> curr = this.head;
		StringBuilder str = new StringBuilder(); 
		str.append("\n{"); 
		
		do
		{
			str.append("Data:"+curr.data+" ");
			curr=curr.nextDuoNode;
		}
		while(curr!=this.head);
		str.append("}");
		
		return str.toString();
		
	}
	
}
