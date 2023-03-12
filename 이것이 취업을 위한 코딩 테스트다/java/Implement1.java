package algorithm_study;

import java.util.*;

public class Implement1 {

	public static void main(String[] args) {
		
		Scanner scanner  = new Scanner(System.in);
		int n = scanner.nextInt();
		scanner.nextLine();
		String[] order = scanner.nextLine().split(" ");

		int[]loc = {1, 1};
		for (int i = 0; i < order.length ; i++)
		{
			if ((order[i].equals("L")) && (loc[1] > 1))
				loc[1]-=1;
			else if ((order[i].equals("R")) && (loc[1] < n))
				loc[1]+=1;
			else if ((order[i].equals("U")) && (loc[0] > 1))
				loc[0]-=1;
			else if ((order[i].equals("D")) && (loc[0] < n))
				loc[0]+=1;
		}
		
		System.out.print(loc[0] + " " + loc[1]);
	}

}
