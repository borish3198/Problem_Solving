package algorithm_study;

import java.util.*;

public class Binary1 {
	
	public static Scanner sc;
	public static int n;
	public static int[] parts;
	public static int m;

	
	public static void binary(int target, int start, int end) {
		
		int mid = (start + end) / 2;
		if (parts[mid] == target) {
			System.out.print("yes ");
			return;
		}
		if (start > end) {
			System.out.print("no ");
			return;
		}
		
		if (target > parts[mid]) {
			start = mid + 1;
			binary(target, start, end);
		}
		else {
			end = mid - 1;
			binary(target, start, end);
		}
			
	}

	public static void main(String[] args) {
		
		sc = new Scanner(System.in);
		n = sc.nextInt();

		parts = new int[n];
		for (int i = 0 ; i < n ; i++)
			parts[i] = sc.nextInt();
		sc.nextLine();
		m = sc.nextInt();
		Arrays.sort(parts);

		for (int i = 0 ; i < m ; i++) {
			int target = sc.nextInt();
			binary(target, 0, n - 1);		
		}
		
	}

}
