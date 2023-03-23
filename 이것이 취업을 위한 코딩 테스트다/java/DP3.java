package algorithm_study;

import java.util.*;

public class DP3 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] tiles = new int[n + 1];
		
		tiles[1] = 1;
		tiles[2] = 1;
		for (int i = 3; i <= n; i++) {
			tiles[i] = ((tiles[i - 1] * 2) + tiles[i - 1])%796796; 
		}
		
		System.out.println(tiles[n]);
	}

}
