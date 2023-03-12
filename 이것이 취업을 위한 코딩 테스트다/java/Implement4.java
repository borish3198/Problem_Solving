package algorithm_study;

import java.util.*;

public class Implement4 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		sc.nextLine();
		int x = sc.nextInt();
		int y = sc.nextInt();
		int dir = sc.nextInt();
		sc.nextLine();
		int ans = 1;
		int mvcnt = 0;
		
		int[][] map = new int[m][n];
		for (int i = 0; i < m ; i++) {
			String[] temp = sc.nextLine().split(" ");
			for (int j = 0; j < n ; j++) {
				map[i][j] = Integer.valueOf(temp[j]);
			}
		}
		
		int[] x_mv = {-1, 0, 1, 0};
		int[] y_mv = {0, 1, 0, -1};
		
		while (true) {
//			# 본인이 다녀 간 곳 표시 
			map[x][y] = -1;
			
//			# 시계 반대방향으로 회전 
			dir--;
			if (dir < 0)
				dir = 3;
			mvcnt++;
			
			int nx = x + x_mv[dir];
			int ny = y + y_mv[dir];
			
//			# 새로운 방향의 맵 확인 
			if (map[nx][ny] == 1 || map[nx][ny] == -1)
			{
//				# 사방이 모두 다녀왔거나 바다인 경우 
				if (mvcnt == 4)
				{
					nx = x + x_mv[(dir + 2) % 4];
					ny = y + y_mv[(dir + 2) % 4];
//					# 후진할 곳이 있는 경우 
					if (map[nx][ny] <= 0) {
						mvcnt = 0;
						x = nx;
						y = ny;
						continue;
					}
					else
						break;
				}	
				continue;
			}
//			# 갈 곳이 있는 경우 
			else {
				x = nx;
				y = ny;
				ans++;
				mvcnt = 0;
				continue;
			}
			
		}
		System.out.println(ans);
	}
}
