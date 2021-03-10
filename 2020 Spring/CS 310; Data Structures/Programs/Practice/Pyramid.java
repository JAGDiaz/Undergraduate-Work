package Practice;

import java.util.Scanner;

class pyramid
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int n;
		System.out.print("Enter a natural number for the Pyramid!!!: ");
		do{
			while(!input.hasNextInt())
			{
				System.out.printf("\"%s\" is not a natural number!\n", input.next());	
				System.out.print("Enter a natural number for the Pyramid!!!: ");
			}
			n = input.nextInt();
		}while(n < 1);
		for(int i = 1; i <= n; i++)
		{
			for(int j = 1; j <= i; j++)
			{
				System.out.printf("%d", j);
			}
			System.out.println();
		}	
	}	
}
