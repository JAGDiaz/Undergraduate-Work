package Practice;

import java.util.Scanner;

class euclid
{
	public static void main(String[] args)
	{
		int m = 0, n = 0, r = 1, m1, n1;
		String wrong;
		Scanner input = new Scanner(System.in);
		System.out.println("Euclid's Algorithm!");
		System.out.print("Please enter the first integer: ");
		do{
			while(!input.hasNextInt())
			{
				wrong = input.next();
				System.out.printf("\"%s\" is not an integer!\n", wrong);
				System.out.print("Please enter the first integer: ");
			}
			m = input.nextInt();
		}while(m < 1);
		System.out.print("\nPlease enter the second integer: ");
		do{
			while(!input.hasNextInt())
			{
				wrong = input.next();
				System.out.printf("\"%s\" is not an integer!\n", wrong);
				System.out.print("\nPlease enter the second integer: ");
			}
			n = input.nextInt();
		}while(n < 1);

		if(n > m)
   		{
			m1 = n;
			n1 = m;
		}
		else
		{
			m1 = m;
			n1 = n;
		}
		while(r != 0)
		{
			r = m1 % n1;
			if(r != 0)
			{
				m1 = n1;
				n1 = r;
			}
		}
		System.out.printf("The GCD of %d and %d is %d.\n", m, n, n1);
	}
}
