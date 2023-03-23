package algorithm_study;

import java.util.*;

public class DP1 {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int[] list = new int[300001];
		int n = sc.nextInt();
	
		for (int i = 2; i <= n ; i ++) {
			list[i] = list[i - 1] + 1;
			if (i % 5 == 0)
				list[i] = Math.min(list[i/5] + 1, list[i]);
			else if (i%3 == 0)
				list[i] = Math.min(list[i/3] + 1, list[i]);
		}
		
		System.out.println(list[n]);
	}

}
