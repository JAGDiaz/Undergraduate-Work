package progassign01.Container;

import progassign01.Interface.StackSpecs;

public class LLStack<E> implements StackSpecs<E>
{
	
	private Node<E> top;
	private int stackSize;
	
	public LLStack()
	{
		this(null, 0);
	}
	public LLStack(Node<E> top, int stackSize)
	{
		this.top = top;
		this.stackSize = stackSize;
	}

	@Override
	public boolean isEmpty() 
	{
		return this.getStackSize() == 0;
	}
	
	@Override
	public void emptyStack() 
	{
		if(!this.isEmpty())
		{
			this.setTop(null);
			this.setStackSize(0);
		}
	}
	@Override
	public void push(E obj) 
	{
		if(this.isEmpty())
		{
			this.setTop(new Node<E>(obj));
			this.setStackSize(this.getStackSize() + 1);
		}
		else
		{
			Node<E> temp = new Node<E>(obj);
			temp.setNextNode(this.top);
			this.setTop(temp);
			this.setStackSize(this.getStackSize() + 1);
		}
	}
	@Override
	public E pop() 
	{
		if(this.isEmpty())
			return null;
		else	
		{
			Node<E> temp = this.getTop();
			this.setTop(this.getTop().getNextNode());
			this.setStackSize(this.getStackSize() - 1);
			return temp.getData();
		}
	}
	@Override
	public E peek() 
	{
		return this.getTop().getData();
	}
	
	@Override
	public String toString()
	{
		if(this.isEmpty())
		{
			return "Empty.";
		}
		else
		{
			LLStack<E> tempStack = new LLStack<E>();
			E tempData;
			
			String name = "[ ";
			while(!this.isEmpty())
			{
				tempData = this.pop();
				name += tempData.toString() + " ";
				tempStack.push(tempData);
			}
			
			while(!tempStack.isEmpty())
				this.push(tempStack.pop());

			return name  + "]";
		}
	}
	public String gnirtSot()
	{
		if(this.isEmpty())
		{
			return "Empty.";
		}
		else
		{
			LLStack<E> tempStack = new LLStack<E>();
			E tempData;
			
			String name = "[ ";
			while(!this.isEmpty())
				tempStack.push(this.pop());
			
			while(!tempStack.isEmpty())
			{
				tempData = tempStack.pop();
				name += tempData.toString() + " ";
				this.push(tempData);
			}

			return name  + "]";
		}
		
	}
	
	public Node<E> getTop()
	{
		return this.top;
	}
	public void setTop(Node<E> newTop)
	{
		this.top = newTop;
	}
	public int getStackSize()
	{
		return this.stackSize;
	}
	public void setStackSize(int stackSize)
	{
		this.stackSize = stackSize;
	}

}
