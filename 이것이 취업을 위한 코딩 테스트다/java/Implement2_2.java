package algorithm_study;

import java.util.*;

public class Implement2_2 {

	public static boolean check(int h, int m, int s){
		if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3)
		{
			return true;
		}
		return false;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int ans = 0;
		for (int i = 0 ; i <= N ; i++) {
			for (int j = 0 ; j < 60 ; j++) {
				for (int k = 0 ; k < 60 ; k++) {
					if (check(i, j, k))
						ans++;
				}
			}
		}
		System.out.println(ans);
	}
}
