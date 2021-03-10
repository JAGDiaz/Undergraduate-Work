package ArrayImplementations;
import java.util.Scanner;

public class main
{
	public static void main(String[] args)
	{
		QueueArray<Integer> numqueue = new QueueArray<Integer>();
		int i = 0;

   		Scanner myObj = new Scanner(System.in); 
		do
		{
	    		int choice = Integer.parseInt(myObj.next());
	   		if (choice < 35) 
	   			numqueue.enqueue(choice);
	   		i++;
		}while (i<10);

		do
		{
			System.out.println("Dequeued from the Queue: " 
						+ numqueue.dequeue());
		}while (numqueue.isEmpty()==false);

	}
}

