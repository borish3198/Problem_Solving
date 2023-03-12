package algorithm_study;

import java.util.*;

public class Greedy2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		
		int N = scanner.nextInt();
		int M = scanner.nextInt();
		int K = scanner.nextInt();
		int ans = 0;
		
		int[] arr = new int[N];
		for (int i = 0; i < N ; i++)
		{
			arr[i] = scanner.nextInt();
		}
		
		Arrays.sort(arr);
		ans += arr[N-1] * (M - (M/(K+1)));
		ans += arr[N-2] * (M/(K+1));
		System.out.println(ans);
	}

}
