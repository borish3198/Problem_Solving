package algorithm_study;

import java.util.*;

public class Greedy1 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int cnt = 0;
		int[] coin = {500, 100, 50, 10};
		
		for (int div : coin)
		{
			cnt += N / div;
			N = N % div;
		}
		
		System.out.println(cnt);
		scanner.close();
	}

}
