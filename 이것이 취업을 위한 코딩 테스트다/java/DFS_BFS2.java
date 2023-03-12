package algorithm_study;

import java.util.*;

public class DFS_BFS2 {

	public static int n, m;
	
	public static boolean check(int x, int y) {
		if ((x >= 0 && x < n) && (y >= 0 && y < m))
			return true;
		return false;
	}
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		sc.nextLine();
		int[][] map = new int[n][m];
		int[][] visited = new int[n][m];
		int[] x_move = {0, 0, 1, -1};
		int[] y_move = {1, -1, 0, 0};
		
		for (int i = 0; i < n ; i++) {
			String temp = sc.next();
			for (int j = 0; j < m; j++) {
				map[i][j] = temp.charAt(j) - '0';
			}
		}
		Queue queue = new LinkedList<>();
		int[] loc = {0, 0};
		queue.add(loc);
		visited[0][0] = 1;
		
		while (!queue.isEmpty()) {
			int[] temp = (int[]) queue.poll();
			for (int i = 0 ; i < 4 ; i++) {
				int nx = temp[0] + x_move[i];
				int ny = temp[0] + y_move[i];
				if (check(nx, ny) && visited[nx][ny] == 0) {
					visited[nx][ny] = visited[temp[0]][temp[1]] + 1;
					temp[0] = nx;
					temp[1] = ny;
					queue.add(temp);
				}
			}
		}
		System.out.println(visited[n-1][m-1]);
		
	}

}
