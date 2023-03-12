package algorithm_study;

import java.util.*;

public class DFS_BFS1 {
	
	public static int n, m;
	
	private static boolean makeIcecream(int x, int y, int[][] map) {
		int[] x_move = {0, 0, 1, -1};
		int[] y_move = {1, -1, 0, 0};
		
		if (map[x][y] == 1)
			return false;
		
		map[x][y] = 1;
		for (int i = 0; i < 4; i++) {
			int nx = x + x_move[i];
			int ny = y + y_move[i];
			if ((nx >= 0 && nx < n) && (ny >= 0 && ny < m)) {
				makeIcecream(nx, ny, map);
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		sc.nextLine();
		int ans = 0;
		
		int[][] map = new int[n][m];
		for (int i = 0; i < n; i++) {
			String temp = sc.next();
			for (int j = 0; j < m; j++)
				map[i][j] = temp.charAt(j) - '0';
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j<m; j++) {
				if (makeIcecream(i, j, map))
					ans++;
			}
		}
		System.out.println(ans);		
	}

}
