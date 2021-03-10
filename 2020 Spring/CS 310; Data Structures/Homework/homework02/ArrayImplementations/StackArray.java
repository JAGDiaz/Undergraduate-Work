package ArrayImplementations;

public class StackArray<E> 
{
			
		private int top=-1;
		private static final int MAX_ITEMS = 10;
		private E items[];

		@SuppressWarnings("unchecked")
		public StackArray() {
			items = (E[]) new Object[MAX_ITEMS];
			System.out.println("Stack Created!");
		}

		public void push(E e) {
			if (isFull()==true) {
			   System.out.println("Stack Full!");
			}
			else{
				top=top+1;
				items[top] = e;
			}
		}


		public E pop() {
			 if (isEmpty()==true) {
				   System.out.println("Stack Empty!");
				}
			 else{
			
			E e = (E) items[top];
			items[top] = null;
			top = top-1;
			return e;
			 }
			return null;
		}

		public boolean isFull() {
			 if (top == items.length-1) {
				 return true;
			 }
			 return false;
		}

		public boolean isEmpty(){
			 if (top==-1) {
				 return true;
			 }
			 return false;
		}

		public E peek()
		{
			return this.items[this.top];
		}

		public void countPosNeg()
		{
			int temp, posiCount = 0, negaCount = 0;
			StackArray<Integer> tempStack = new StackArray<Integer>();
			while(!this.isEmpty())
			{
				temp = (int)this.pop();
				
				if(temp > 0)
					posiCount++;
				else if(temp < 0)
					negaCount++;
					
				tempStack.push(temp);
			}
			
			while(!tempStack.isEmpty())
				this.push((E)tempStack.pop());
				
			tempStack = null;
			System.out.printf("There are %d positive numbers and %d", posiCount, negaCount);
			System.out.println(" negative numbers in this stack.");
		}

		public boolean sameStack(StackArray<E> s2)
		{
			if(this.top != s2.top)
				return false;
				
			if(this.isEmpty() && s2.isEmpty())
				return true;
			
			boolean temp;
			if(this.peek().equals(s2.peek()))
			{
				E temp1 = this.pop();
				E temp2 = s2.pop();
				temp = this.sameStack(s2);
				this.push(temp1);
				s2.push(temp2);
			}
			else
				return false;

			return temp;
		}

		@Override
		public String toString()
		{
			System.out.println("Array:");
			System.out.print("{");
			 for(int i = 0; i < items.length ;i++) {
				 System.out.print(items[i]+" ");
		}
			 System.out.print("}");
			return "";
		}
		public static void main(String[] args) 
		{
			
			// Code reference for countPosNeg method
			StackArray<Integer> intStack = new StackArray<Integer>();
				intStack.push(10);
				intStack.push(10);
				intStack.push(30);
				intStack.push(-40);
			// call countPosNeg here
				intStack.countPosNeg();
				System.out.println("intStack before counting");
				System.out.println(intStack);
			
			 System.out.println("intStack after counting");
				System.out.println(intStack);
				
			// Code reference for sameStack method
		   StackArray<Integer> stack = new StackArray<Integer>();
		   StackArray<Integer> stack2 = new StackArray<Integer>();

			stack.push(10);
			stack.push(20);
			stack.push(30);
			stack.push(40);
			stack2.push(10);
			stack2.push(20);
			stack2.push(30);
			stack2.push(40);
			 
		   
			System.out.println(stack);
			System.out.println(stack2);
			
			//Calling comparison method
		   System.out.println(stack.sameStack(stack2)); 
		}

				
				
}
