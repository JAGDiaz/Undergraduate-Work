package Practice;

import java.util.Scanner;

class sum
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int n, sum = 0;
		String wrong;
		System.out.print("Enter a natural number for the sum of [n]: ");
		do{
			while(!input.hasNextInt())
			{
				wrong = input.next();
				System.out.printf("\"%s\" is not a natural number!\n", wrong);	
				System.out.print("Enter a natural number for the sum of [n]: ");
			}
			n = input.nextInt();
		}while(n < 1);

		for(int i = 1; i <= n; i++)
		{
			if(i == 1)
				System.out.printf("%d ", i);
			else
				System.out.printf("+ %d ", i);

			if(i % 20 == 0)
				System.out.println();

			sum += i;
		}	
		System.out.printf("= %d\n", sum);		
	}	
}
