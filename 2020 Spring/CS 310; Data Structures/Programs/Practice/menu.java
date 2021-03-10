package Practice;

import java.util.Scanner;
import java.util.Random;

class menu
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		char opt;
		int n;
		System.out.print("Please enter a natural number for the length of the array: ");
		do{
			while(!input.hasNextInt())
			{
				System.out.printf("\"%s\" isn't a natural number!\n", input.next());
				System.out.print("Please enter a natural number for the length of the array: ");
			}
			n = input.nextInt();
		}while(n < 1);
		int[] numbers = populate(n);
		do{
			System.out.println("(A)			Print ascending");
			System.out.println("(D)			Print descending");
			System.out.println("(R)			Repopulate");
			System.out.println("(Q)			Quit");
			System.out.print("\nPlease make your selection: ");
			opt = input.next().charAt(0);
			System.out.println();
			switch(opt)
			{		
				case 'A':
				case 'a':
							System.out.print("[ ");
							ascend(numbers, 0);
							System.out.println("]\n");
							break;

				case 'D':
				case 'd':
							System.out.print("[ ");
							descend(numbers, 0);
							System.out.println("]\n");
							break;

				case 'R':
				case 'r':
							numbers = populate(n);
							System.out.println("The array has been repopulated.\n");
							break;

				case 'Q':
				case 'q':
							System.out.println("Thanks for joining!\n");
							break;

				default:
							System.out.println("Invalid Selection, please make another selection.");
			}
		}while(opt != 'q' && opt != 'Q');
	}
	public static int[] populate(int n)
	{
		Random rand = new Random(System.currentTimeMillis() / 1000L);
		int[] numbers = new int[n];
		for(int i = 0; i < n; i++)
		{
			numbers[i] = rand.nextInt() % 666;
		}
		return numbers;
	}
	public static void ascend(int[] num, int n)
	{
		if(n != num.length)
		{
			System.out.printf("%d ", num[n]);
			ascend(num, n + 1);
		}
			
	}
	public static void descend(int[] num, int n)
	{
		if(n != num.length)
		{
			descend(num, n + 1);
			System.out.printf("%d ", num[n]);
		}
	}
	
}
