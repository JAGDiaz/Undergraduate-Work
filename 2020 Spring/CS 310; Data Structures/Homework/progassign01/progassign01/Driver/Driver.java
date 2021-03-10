package progassign01.Driver;

import progassign01.Container.StackQ;
import progassign01.Data.DataClass;
import java.util.Scanner;
import java.lang.Exception;

public class Driver 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);	
		StackQ<DataClass> stq = new StackQ<DataClass>();
		char selection;	
		int idTemp;
		String nameTemp;

		do
		{

			generateMenu();

			selection = validateChar(input);		

			switch(selection)
			{

				case 'a':
				case 'A':
						System.out.print("\n\tPlease enter a valid ID: ");
						idTemp = validateInteger(input);
						System.out.print("\tPlease enter the name: ");
						nameTemp = input.nextLine();
						stq.enQ(new DataClass(nameTemp, idTemp));
						System.out.printf("\n\t%s has been added to the Queue.\n", nameTemp);
						break;

				case 'b':
				case 'B':
						if(!stq.isEmpty())
							System.out.printf("\n\t%s has been dequeued.\n\n", stq.deQ().toString());
						else
							System.out.println("\n\tThe Queue is empty.\n");
						break;

				case 'c':
				case 'C':
						if(!stq.isEmpty())
							System.out.printf("\n\t%s is at the front of the Queue.\n", stq.peek().toString());
						else
							System.out.println("\n\tThe Queue is empty.\n");
						break;

				case 'd':
				case 'D':
						System.out.printf("\n\t%s\n", stq.toString());
						break;

				case 'e':
				case 'E':
						System.out.printf("\n\tDequeue Stack: %s", stq.showDeQStack());
						System.out.printf("\n\tEnqueue Stack: %s\n", stq.showEnQStack());
						break;
				
				case 'f':
				case 'F':
						System.out.printf("\n\tThere are %d item(s) in the Queue.\n", stq.getQueueSize());
						break;

				case 'g':
				case 'G':
						if(!stq.isEmpty())
						{
							stq.emptyQueue();
							System.out.println("\n\tThe Queue is now empty.\n");
						}
						else
							System.out.println("\n\tThe Queue is already empty.\n");
						break;

				case 'h':
				case 'H':
						System.out.println("\n\tThanks for using Joe-Tech!\n");
						break;
						
				default:
						System.out.println("\n\tInvalid selection, please make a valid selection.\n");
			}
		}while(selection != 'h' && selection != 'H');
	}

	public static void generateMenu()
	{
		
		System.out.println("\nQueue Menu:\n");
			
		System.out.print("\ta. Enqueue\n" +
						 "\tb. Dequeue\n" +
						 "\tc. Peek the Queue\n" +
						 "\td. Display the Queue\n" +
						 "\te. Display enQStack and deQStack\n" +
						 "\tf. Display the size of Queue\n" +
						 "\tg. Empty the Queue\n" +
						 "\th. Exit\n\n" + 
						 "\tPlease make your selection: ");
	}

	public static char validateChar(Scanner input)
	{
		String temp;
		temp = input.nextLine().trim();
		if(temp.length() == 1)
		{
			return temp.charAt(0);
		}
		else
		{
			return '0';
		}
	}
	
	public static int validateInteger(Scanner input)
	{
		int out = 0;
		String temp = "";
		do
		{
			try
			{
				temp = input.nextLine().trim();
				out = Integer.parseInt(temp);
			}
			catch(Exception e)
			{
				
				System.out.printf("\t\"%s\" is not a valid ID.\n", temp);
				System.out.print("\tValid IDs are positive integers with no spaces.\n\n"
									+ "\tPlease re-enter: ");
				out = 0;
				continue;
			}
			finally
			{
				
			}
			if(out < 1)
			{
				System.out.printf("\t\"%s\" is not a valid ID.\n", temp);
				System.out.print("\tValid IDs are positive integers with no spaces.\n\n"
									+ "\tPlease re-enter: ");
			}
		}while(out < 1);
		return out;
	}

}
