package algorithm_study;

import java.util.*;

public class Greedy4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int K = sc.nextInt();
		int cnt = 0;
		
		while (N >= K)
		{
			if (N % K == 0)
			{
				N /= K;
				cnt += 1;
			}
			else
			{
				cnt += (N % K);
				N -= (N % K);
			}
		}
		System.out.println(cnt + N - 1);
	}

}
