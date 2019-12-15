import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    private static int MAX_DIST = 10000;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.nextLine();
        for (int i = 0; i < n; i++) {
            int[][] g = parse(in);
            System.out.println(solve(g));
        }
    }

    private static int[][] parse(Scanner in) {
        int[][] g = new int[100][100];

        in.nextLine();

        for (int i = 0; i < 100; i++) {
            Arrays.fill(g[i], MAX_DIST);
        }

        parseEdges(g, in.nextLine());
        parseEdges(g, in.nextLine());

        for (int i = 0; i < 100; i++) {
            boolean ladderOrSnake = false;
            for (int j = 0; j < 100; j++) {
                if (g[i][j] != MAX_DIST) {
                    ladderOrSnake = true;
                }
                break;
            }
            if (ladderOrSnake) {
                continue;
            }
            for (int j = 1; j < 7; j++) {
                g[i][Math.min(i + j, 99)] = 1;
            }
        }

        return g;
    }

    private static void parseEdges(int[][] g, String edges) {
        String[] edgesArray = edges.split(" ");
        for (String edge : edgesArray) {
            String[] coords = edge.split(",");
            g[Integer.parseInt(coords[0])-1][Integer.parseInt(coords[1])-1] = 0;
        }
    }

    public static int solve(int[][] g) {
        int[] ds = new int[100];

        Arrays.fill(ds, MAX_DIST);
        ds[0] = 0;

        PriorityQueue<Integer> q = new PriorityQueue<Integer>();
        q.add(0);

        while(!q.isEmpty()) {
            Integer node = q.poll();

            int distToNode = ds[node];
            if (distToNode == MAX_DIST) {
                break;
            }

            for (int i = 0; i < 100; i++) {
                int d = g[node][i];
                if (d != MAX_DIST) {

                    int altD = d + distToNode;
                    if (altD < ds[i]) {

                        ds[i] = altD;
                        q.add(i);
                    }
                }
            }
        }
        return ds[99];
    }


}