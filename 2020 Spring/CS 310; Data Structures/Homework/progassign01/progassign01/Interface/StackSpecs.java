package progassign01.Interface;

public interface StackSpecs<E> 
{
	public boolean isEmpty();
	public void emptyStack();
	public void push(E obj);
	public E pop();
	public E peek();
}
