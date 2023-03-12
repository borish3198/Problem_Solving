package algorithm_study;

import java.util.*;

public class Implement2 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int ans = 0;
		
		for (int i = 0 ; i <= N ; i++)
		{
			if ((i == 3) || (i == 13) || (i == 23))
				ans += 3600;
			else
				ans = ans + (15 * 60) + (15 * 45);
		}
		System.out.println(ans);
	}

}
