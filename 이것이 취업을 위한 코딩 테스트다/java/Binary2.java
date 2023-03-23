package algorithm_study;

import java.util.*;


public class Binary2 {
	
	public static int n;
	public static int m;
	public static int[] rices;
	
	public static int binary(int target, int start, int end, int len) {
		
		int mid = (start + end) / 2;
		System.out.println("mid : " + mid);
		if (start > end)
			return mid;
		
		int left = 0;
		for (int i = 0; i < len; i++) {
			int rice = rices[i] - mid;
			if (rice > 0)
				left += rice;
		}
		if (left == target)
			return mid;
		if (left > target) {
			start = mid + 1;
			return binary(target, start, end, len);
		}
		else {
			end = mid - 1;
			return binary(target, start, end, len);
		}
	}
	
	public static void main(String args[]) {
	
		
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		rices = new int[n];
		
		int max = 0;
		for (int i = 0; i < n; i++) {
			int temp = sc.nextInt();
			rices[i] = temp;
			if (temp > max)
				max = temp;
		}
		int answer = binary(m, 0, max, n);
		System.out.println(answer);
	}

}
