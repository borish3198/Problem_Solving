package algorithm_study;

import java.util.*;

public class DP4 {

	public static int n;
	public static int m;
	public static int[] coin;
	public static int[] money;
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		coin = new int[n];
		money = new int[10001];
		
		for (int i = 0; i < 10001; i++) {
			money[i] = -1;
		}
		for (int i = 0; i < n; i++) {
			coin[i] = sc.nextInt();
			money[coin[i]] = 1;
			sc.nextLine();
		}
		Arrays.sort(coin);
		
		money[0] = 0;
		for (int i = 0; i <= m; i++) {
			if (i - coin[0] >= 0 && money[i - coin[0]] != -1)
				money[i] = money[i - coin[0]] + 1;
			for (int j = 1; j < n; j++) {
				if (i - coin[j] >= 0 && money[i - coin[j]] != -1)
					money[i] = Math.min(money[i], money[i - coin[j]] + 1);
				
			}
		}

		System.out.println(money[m]);
	}

}
