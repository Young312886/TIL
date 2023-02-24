package SWEA;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class 영준이 {
    static int[] Tree;
    static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int testcase = 1; testcase < T + 1; testcase++) {
            int node = Integer.parseInt(br.readLine());
            StringTokenizer stk = new StringTokenizer(br.readLine());
            Tree = new int[node];
            ArrayList<ArrayList<Integer>> graph = new ArrayList<>(node);
            for (int j = 0; j < node - 1; j++) {
                int parent = Integer.parseInt(stk.nextToken());
                Tree[j + 1] = parent;
                graph.get(parent).add(j + 1);
            }
            answer = 0;
            answer++;
            int start, next;
            start = 1;
            while
            for (int j = 1; j < node - 1; j++) {
                answer += GoingUp(j, j + 1);
            }
            System.out.printf("#%d %d", testcase, answer);
        }
    }

    static int GoingUp(int start, int next) {
        if (Tree[start] == Tree[next]) {
            return 2;
        } else if (Tree[start] == 1 || Tree[next] == 1) {
            return 3;
        } else {
            return GoingUp(Tree[start], Tree[next]) + 2;
        }
    }

}
