package progassign01.Container;

import progassign01.Interface.QueueSpecs;

public class StackQ<E> implements QueueSpecs<E>
{
	
	private LLStack<E> enQStack;
	private LLStack<E> deQStack;

	public StackQ()
	{
		this.enQStack = new LLStack<E>();
		this.deQStack = new LLStack<E>();
	}

	@Override
	public boolean isEmpty() 
	{
		return this.enQStack.isEmpty() && this.deQStack.isEmpty();
	}

	@Override
	public void emptyQueue() 
	{
		this.enQStack.emptyStack();
		this.deQStack.emptyStack();
	}

	@Override
	public void enQ(E obj) 
	{
		this.enQStack.push(obj);	
	}

	@Override
	public E deQ() 
	{
		if(this.isEmpty())
			return null;
		else 		
		{	
			if(this.deQStack.isEmpty())
				this.reStack();
			return this.deQStack.pop();
		}
	}

	@Override
	public E peek() 
	{
		if(this.isEmpty())
			return null;
		else 		
		{	
			if(this.deQStack.isEmpty())
				this.reStack();
			return this.deQStack.peek();
		}
	}
	
	@Override
	public String toString()
	{
		if(this.isEmpty())
			return "The Queue is Empty.";
		else if(this.deQStack.isEmpty())
			return this.enQStack.gnirtSot();
		else if(this.enQStack.isEmpty())
			return this.deQStack.toString();
		else
			return (this.deQStack.toString() + this.enQStack.gnirtSot()).replace("][ ", "");
	}
	
	private void reStack()
	{
		while(!this.enQStack.isEmpty())
		{
			this.deQStack.push(this.enQStack.pop());
		}
	}
	public int getQueueSize()
	{
		return this.enQStack.getStackSize() + this.deQStack.getStackSize();
	}

	public String showEnQStack()
	{
		return this.enQStack.gnirtSot();
	}

	public String showDeQStack()
	{
		return this.deQStack.toString();
	}
}
