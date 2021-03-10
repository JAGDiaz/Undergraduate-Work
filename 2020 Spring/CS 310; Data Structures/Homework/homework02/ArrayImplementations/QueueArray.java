package ArrayImplementations;

import java.util.Arrays;
import java.util.Scanner;

public class QueueArray<E> {
	
		private int currentSize; 
	    private E[] queueElements;
	    private static final int MAX_ITEMS = 10; 

	    private int rear;
	    private int front; 
	    @SuppressWarnings("unchecked")
		public QueueArray() {
	      
	        queueElements = (E[]) new Object[MAX_ITEMS];
	        currentSize = 0;
	        front = -1;
	        rear = -1;
	    }

	    public void enqueue(E item){
	        if (isFull()) {
	          System.out.println("Queue is Full");
	        }
	        else {
	            if(rear == queueElements.length)
	            	rear=0;
	            else
	            	rear=rear+1;
	            
	            queueElements[rear] = item;
	            currentSize++;
	            
	            if (front == -1) {
					front = rear;
				}
	        }
	    }

	
	    public E dequeue(){
	        E dequeueItem = null;
	        if (isEmpty()) {
	            System.out.println("Queue is Empty!");
	        }
	        else {
	        	dequeueItem = queueElements[front];
	            queueElements[front++] = null;
	            if(front==queueElements.length)
	            	front=0;
	            if(isEmpty()==true)
	            	front = rear = -1;
	            currentSize--;
	        }
	        return dequeueItem;
	    }

	    public boolean isFull() {
	        return (currentSize == queueElements.length);
	    }

	  
	    public boolean isEmpty() {
	        return (currentSize == 0);
	    }

	    @Override
	    public String toString() {
	        return "CircularQueue [" + Arrays.toString(queueElements) + "]";
	    }
	    
	   


	}



	


