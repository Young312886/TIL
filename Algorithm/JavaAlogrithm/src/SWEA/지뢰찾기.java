package SWEA;

import java.util.*;

public class 지뢰찾기 {
    static int N;
    static int[][] ground;
    static final int[] dr = {-1, 1, 0, 0, -1, -1, 1, 1}, dc = {0, 0, -1, 1, 1, -1, -1, 1};

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        for (int testcase = 1; testcase < T + 1; testcase++) {
            N = sc.nextInt();
            ground = new int[N][N];
            for (int i = 0; i < N; i++) {
                String oneline = sc.next();
                for (int j = 0; j < N; j++)
                    if (String.valueOf(oneline.charAt(j)).equals("*")) {
                        ground[i][j] = -2;
                    } else ground[i][j] = -1;
            }
            int answer = solve();
            System.out.printf("#%d %d%n", testcase, answer);
        }

    }

    static int solve() {
        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (ground[i][j] != -1) continue;
                else {
                    if (IsZero(i, j)) {
                        Deque<int[]> stack = new ArrayDeque<>();
                        int[] start = {i, j};
                        stack.addFirst(start);
                        while (!stack.isEmpty()) {
                            int[] point = stack.removeFirst();
                            int si = point[0];
                            int sj = point[1];
                            ground[si][sj] = 0;
                            for (int delta = 0; delta < 8; delta++) {
                                int ni = si + dr[delta];
                                int nj = sj + dc[delta];
                                if (0 > ni || ni >= N || 0 > nj || nj >= N || ground[ni][nj] != -1) continue;
                                if (IsZero(ni, nj)) stack.add(new int[]{ni, nj});
                                ground[ni][nj] = 0;
                            }
                        }
                        answer++;
                    }
                }
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (ground[i][j] == -1) answer++;
            }
        }
        return answer;
    }

    static boolean IsZero(int ni, int nj) {
        for (int delta = 0; delta < 8; delta++) {
            int di = ni + dr[delta];
            int dj = nj + dc[delta];
            if (di < 0 || dj < 0 || di >= N || dj >= N) continue;
            if (ground[di][dj] == -2)
                return false;
        }
        return true;
    }

}
