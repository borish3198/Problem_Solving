package algorithm_study;

import java.util.*;

public class Implement3 {

	public static boolean check(int x, int y) {
		if (x > 0 && x < 9 && y > 0 && y < 9)
			return true;
		return false;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String loc = sc.nextLine();
		int y = loc.charAt(0) - 'a' + 1;
		int x = loc.charAt(1) - '1' + 1;
		int cnt = 0;
		
		int[] x_move = {1, -1, 1, -1, -2, -2, 2, 2};
		int[] y_move = {-2, -2, 2, 2, 1, -1, 1, -1};
		
		for (int i = 0; i < 8 ; i++)
		{
			if (check(x + x_move[i], y + y_move[i]))
				cnt++;
		}
		
		System.out.println(cnt);
	}

}
