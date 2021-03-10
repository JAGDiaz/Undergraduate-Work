package priorityqueues;

public interface PriorityQueueInterface<E> {
	
	public void insertItem(E data,int priority);
	public E removeMin();
	public boolean isEmpty();
	public E minElement(); /* Equal to peek*/
	public int minPriority();
	public void display();

}
