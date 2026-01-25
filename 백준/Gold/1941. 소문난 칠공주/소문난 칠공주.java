import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

public class Main {
    static final int SIZE = 5;
    static char[] grid = new char[SIZE * SIZE];
    static int[] selected = new int[7];
    static int answer = 0;

    static void combination(int idx, int cnt, int sCount) {
        if (cnt == 7) {
            if (sCount >= 4) {
                if (isConnected()) answer++;
            }
            return;
        }
        for (int i = idx; i < 25; i++) {
            selected[cnt] = i;
            combination(i + 1, cnt + 1, sCount + (grid[i] == 'S' ? 1 : 0));
        }
    }

    static boolean isConnected() {
        int count = 0;
        boolean[] visited = new boolean[SIZE * SIZE];

        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(selected[0]);

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            int x = cur % 5, y = cur / 5;

            for (int[] d : new int[][] {{1, 0}, {0, 1}, {0, -1}, {-1, 0}}) {
                int nx = x + d[0], ny = y + d[1];
                int nextCur = nx + ny * SIZE;
                if (0 <= nx && nx < SIZE && 0 <= ny && ny < SIZE && !visited[nextCur] && Arrays.stream(selected).anyMatch(n -> n == nextCur)) {
                    visited[nextCur] = true;
                    queue.add(nextCur);
                    count++;
                }
            }
        }

        return count == 7;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < SIZE; i++) {
            System.arraycopy(br.readLine().toCharArray(), 0, grid, i * SIZE, SIZE);
        }

        combination(0, 0, 0);

        System.out.println(answer);
    }
}