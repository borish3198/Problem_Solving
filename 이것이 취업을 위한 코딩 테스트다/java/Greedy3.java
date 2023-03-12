package algorithm_study;

import java.util.*;

public class Greedy3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();

		int[][] card = new int[N][M];
		
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M ; j++)
				card[i][j] = sc.nextInt();
			Arrays.sort(card[i]);
		}

		int[] small_arr = new int[N];
		for (int i = 0 ; i < N ; i++)
			small_arr[i] = card[i][0]; 

		Arrays.sort(small_arr);
		System.out.println(small_arr[N - 1]);
	}

}
