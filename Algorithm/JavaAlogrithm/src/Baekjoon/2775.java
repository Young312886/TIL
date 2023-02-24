import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] floor = new int[k+1];
            for (int p = 0; p <= k; p++) {
                floor[p] = p;
            }
            for (int j = 0; j < n; j++) {
                for (int base = 1; base <= k; base++) {
                    floor[base] += floor[base-1];
                }
            }
            System.out.println(floor[k]);
        }

    }
}