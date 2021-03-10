package PQHeaps;
import java.util.*;
public class Heap 
{
	
	private int[] a;
	private int n;
	public Heap()
	{
		a=new int[1];
		n=0;
		a[0]=Integer.MAX_VALUE;
	}
	
	public Heap(int maxSize)
	{
		a= new int[maxSize];
		n=0;
		a[0]=Integer.MAX_VALUE;
	}
	public int getMaxSize()
	{
		return this.a.length;
	}
	public void insertItem(int value)
	{
		n++;
		a[n]=value;
		upHeap(n);
	}
	
	private void upHeap(int i)
	{
		int k=a[i];
		int iparent=i/2;
		while(a[iparent]<k&&iparent!=0)
		{
			a[i]=a[iparent];
			i=iparent;
			iparent=i/2;
		}
		a[i]=k;
	}
	
	public int removeMax()
	{
		if(n==0)
			throw new NoSuchElementException("Heap is Empty!!");
		int maxValue=a[1];
		a[1]=a[n];
		n--;
		downHeap(1);
		return maxValue;
	}
	public void downHeap(int i)
	{
		int k=a[i];
		int left=2*i;
		int right=left+1;
		
		while (right<=n)
		{
			if(k>=a[left]&&k>=a[right])
			{
				a[i]=k;
				return;
			}
			else if(a[left]<a[right])
			{
				a[i]=a[right];
				i=right;
			}
			else
			{
				a[i]=a[left];
				i=left;
			}
			left=2*i;
			right=left+1;
		}
		
		/* If number of nodes is even there is one node without right child */
		if(left==n&&k<a[left])
		{
			a[i]=a[left];
			i=left;
		}
		a[i]=k;
	}
	
	public void max_heapify(int Arr[ ] , int i, int N)
	{
		int left  = 2*i;
		int right = 2*i+1;
		int largest;
		if(left >= N && Arr[left] < Arr[ i ] )
			largest = left;
		else
			largest = i;
		if(right >= N && Arr[right] < Arr[largest])
	    	largest = right;
		if(largest != i)
		{
			int temp=Arr[i];
			Arr[i]=Arr[largest];
			Arr[largest]=temp;
	    	max_heapify(Arr, largest, N);
		} 
	}

	public void printLevels(int i)
	{
		if(i > n || i < 1)
		{	
			System.out.println();
			return;
		}
		int j = i;	
		System.out.println();
		while(j < 2*i && j <= n)
			System.out.printf("%6d", a[j++]);
		printLevels(2*i);

	}

	public boolean isMaxHeap(int i)
	{
		if(2*i > n)
			return true;

		if(a[i] > a[2*i] && a[i] > a[2*i + 1])
			return isMaxHeap(2*i) && isMaxHeap(2*i + 1);
		else
			return false;

	}

	public static void main(String[] args)
	{
		Heap maxHeap = new Heap(100);
		heapFill(maxHeap);
		maxHeap.printLevels(1);
		System.out.println("Max Heap: " + maxHeap.isMaxHeap(1));
		

		System.out.println("\nMax removed: " + maxHeap.removeMax());
		maxHeap.printLevels(1);
		System.out.println("Max Heap: " + maxHeap.isMaxHeap(1));


	}
	public static void heapFill(Heap fillThis)
	{
		Random rand = new Random(System.nanoTime());
		for(int i = 1; i < fillThis.getMaxSize(); i++)
			fillThis.insertItem((rand.nextInt() % 1201) + 1200);
	}
}
