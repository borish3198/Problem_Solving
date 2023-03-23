package algorithm_study;

import java.util.*;

public class DP2 {

	public static int n;
	public static int[] storage;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		storage = new int[n];
		for (int i = 0; i < n; i++)
			storage[i] = sc.nextInt();
		int max = 0;
		for (int i = 2; i < n; i++) {
			storage[i] += storage[i-2];
			if (storage[i] > storage[i - 1])
				max = storage[i];
			else
				max = storage[i - 1];
		}
		
		System.out.println(max);
	}

}
