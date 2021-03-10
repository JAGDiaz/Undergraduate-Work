package progassign02.Sorting;

import java.util.LinkedList;

public interface Sorting<E> {
	 public void insertionSort(LinkedList<E> list, int lowindex, int highindex, boolean reversed);
	 public void quicksort(LinkedList<E> list, int lowindex, int highindex, boolean reversed);
	 public void mergeSortLL(LinkedList<E> list, boolean reversed);
}
