package progassign02.Sorting;

import java.util.LinkedList;
import java.util.Random;
import java.util.Scanner;

public class SortingTest<E extends Comparable<E>> implements Sorting<E>
{

	public static void main(String[] args) 
	{
		SortingTest sorter = new SortingTest<>();
		Scanner input = new Scanner(System.in);
		int[] sizes = {10,50,100,150,300,500,1000,1500,2000,5000};
		String[] sorts = {"InsertionSort", "Quicksort", "MergeSort"};
		boolean[] facts1 = {false, true, false};
		boolean[] facts2 = {false, false, true};
		int choice1, choice2;
		long tic, toc;
		boolean reverse;
		System.out.println("\nNote: This program has no input validation.");
		System.out.println("      Invalid inputs WILL cause a crash.");

		do{
			generateSortMenu();
			choice1 = input.nextInt();
			
			if(choice1 > 0 && choice1 < 4)
			{
				generateSizeMenu();

				choice2 = input.nextInt();

				System.out.print("\nEnter an odd integer for ascending order,\n"
								+"even for descending order: ");
				reverse = input.nextInt() % 2 == 0;

				Integer[] randArr = new Integer[sizes[choice2 - 1]];
				sorter.listFill(randArr, true);

				LinkedList<Integer> randList = new LinkedList<Integer>();


				for(int i = 0; i < randArr.length; i++)
				{
					randList.add(randArr[i]);
				}
		
				System.out.println("\nUnsorted:");
				System.out.println(randList);

				tic = System.nanoTime();
				if(choice1 == 1)
				{
					sorter.insertionSort(randList, 0, randList.size(), reverse);
					System.out.println("\nInsertionSorting...");
				}
				else if(choice1 == 2)
				{
					sorter.quicksort(randList, 0, randList.size()-1, reverse);
					System.out.println("\nQuicksorting...");
				}	
				else
				{
					sorter.mergeSortLL(randList, reverse);
					System.out.println("\nMergeSorting...");
				}

				toc = System.nanoTime();
				System.out.println("\nSorted:");
				System.out.println(randList);
				System.out.printf("\nIn %1.4f milliseconds.\n", (toc - tic)/1e6);
			}
			else if(choice1 == 4)
			{
				for(int k = 0; k < sorts.length; k++)
				{
					System.out.printf("\n\n%s times in milliseconds:\n", sorts[k]);
					System.out.printf("%5s%15s%15s%15s\n","Size", "Sorted",
									  "Unsorted", "Rev. Sorted");
					for(int i = 0; i < sizes.length; i++)
					{
						Integer[] randArr = new Integer[sizes[i]];
						LinkedList<Integer> randList = new LinkedList<Integer>();
						System.out.printf("%5d",sizes[i]);
						for(int j = 0; j < facts1.length; j++)
						{
							sorter.listFill(randArr, facts1[j]);
							for(int w = 0; w < randArr.length; w++)
							{
								randList.add(randArr[w]);
							}
							if(facts2[j])
								sorter.listReverse(randList,0,randList.size());

							tic = System.nanoTime();
							if(choice1 == 1)
								sorter.insertionSort(randList, 0, randList.size(), false);
							else if(choice1 == 2)
								sorter.quicksort(randList, 0, randList.size()-1, false);
							else
								sorter.mergeSortLL(randList, false);
							toc = System.nanoTime();

							System.out.printf("%12.3f ms", (toc-tic)/1e6);
							
						}
						System.out.println();
					}
				}
			}
		}while(choice1 != 5);
		System.out.println("Thanks!");
	}

	public SortingTest()
	{}

	@Override
	public void insertionSort(LinkedList<E> list, int lowindex, int highindex, boolean reversed) 
	{
		if(highindex <= 1)
			return;

		insertionSort(list, lowindex, highindex - 1, reversed);
			
		E last = list.remove(highindex-1);
		int j = highindex - 2;

		while(j >= 0 && list.get(j).compareTo(last) > 0)
			j--;

		list.add(j+1, last);

		if(highindex == list.size() && reversed)
			listReverse(list, lowindex, highindex);

		return;
	}

	@Override
	public void quicksort(LinkedList<E> list, int lowindex, int highindex, boolean reversed) 
	{	
		if(lowindex >= highindex)
			return;

		int alpha = 1, i = lowindex;
		if(reversed)
			alpha = -1;

		E pivot = list.get(highindex);
		for(int j = lowindex; j <= highindex; j++)
		{
			if(alpha*list.get(j).compareTo(pivot) < 0)
			{
				swap(list, i, j);
				i++;
			}	
		}
		swap(list, i, highindex);
	
		quicksort(list, lowindex, i - 1, reversed);
		quicksort(list, i + 1, highindex, reversed);

		return;
	}

	@Override
	public void mergeSortLL(LinkedList<E> list, boolean reversed) 
	{
		if(list.size() <= 1)
			return;
		
		int alpha = 1;
		if(reversed)
			alpha = -1;
		
		LinkedList<E> left = new LinkedList<E>();
		LinkedList<E> right = new LinkedList<E>();
		for(int i = 0; i < list.size(); i++)
		{
			if(i < list.size()/2)
				left.add(list.get(i));
			else
				right.add(list.get(i));
		}

		list.clear();

		mergeSortLL(left, reversed);
		mergeSortLL(right, reversed);
		
		while(left.size() > 0 && right.size() > 0)
		{
			if(left.getFirst().compareTo(right.getFirst()) <= 0)
				list.add(left.pollFirst());
			else
				list.add(right.pollFirst());
		}

		while(left.size() > 0)
			list.add(left.pollFirst());

		while(right.size() > 0)
			list.add(right.pollFirst());

		return;
	}

	public void listFill(Integer[] arr, boolean random)
	{
		if(random)
		{
			Random chance = new Random(System.nanoTime());
			for(int i = 0; i < arr.length; i++)
				arr[i] = new Integer(chance.nextInt() % 5000);
		}
		else
		{
			for(int i = 0; i < arr.length; i++)
				arr[i] = new Integer(i);
		}
	}

	public void listReverse(LinkedList<E> list, int begin, int end)
	{
		if(end - 1 < begin || end - 1 == begin)
			return;
		else
		{
			swap(list, begin, end - 1);
			listReverse(list, begin + 1, end - 1);
			return;
			
		}
	}
	public void swap(LinkedList<E> list, int first, int second)
	{
		if(first != second)
		{
			if(first > second)
			{
				swap(list, second, first);
				return;
			}
			E temp1 = list.remove(second);
			E temp2 = list.remove(first);
			list.add(first, temp1);
			list.add(second, temp2);
		}
		return;
	}

	public static void generateSortMenu()
	{
		
		System.out.println("\nSort Menu:\n");
			
		System.out.print("1. InsertionSort\n" +
						 "2. QuickSort\n" +
						 "3. MergeSort\n" +
						 "4. All\n" +
						 "5. Exit\n\n" + 
						 "Please choose a sorting algorithm: ");
	}

	public static void generateSizeMenu()
	{
		
		System.out.println("\nSize Menu:\n");
			
		System.out.print("1. 10\n" +
						 "2. 50\n" +
						 "3. 100\n" +
						 "4. 150\n" + 
						 "5. 300\n" +
						 "6. 500\n" +
						 "7. 1000\n" + 
						 "8. 1500\n\n" +
						 "Please choose a problem size: ");
	}
}
