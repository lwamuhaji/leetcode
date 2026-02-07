import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

class Main {
    static int[][] board = new int[9][50];
    static int innings;
    static int answer = 0;
    static int[] orders = new int[9];
    static boolean[] visited = new boolean[9];

    /**
     * orders는 선수가 나가는 순서임.
     * 숫자+1이 선수 번호임. (선수 번호는 1번부터 시작)
     * 즉 [3, 0, 1, 2, 3, 4, 5, 6, 7] 이면 4번 선수가 가장 먼저 나가고 8번 선수가 마지막에 나감
     */
    private static int simulate() {
        int score = 0;
        int pos = 0; // 타순 인덱스 (0~8)

        // 이닝별 반복
        for (int curInning = 0; curInning < innings; curInning++) {
            int out = 0;
            // 루상 주자 상태 (1루, 2루, 3루) - 매 이닝 초기화
            boolean b1 = false, b2 = false, b3 = false;

            while (out < 3) {
                // resultOrder[pos]가 현재 타자 번호
                int result = board[orders[pos]][curInning];

                if (result == 0) { // 아웃
                    out++;
                } else if (result == 1) { // 안타
                    if (b3) { score++; b3 = false; }
                    if (b2) { b3 = true; b2 = false; }
                    if (b1) { b2 = true; }
                    b1 = true; // 타자 진루
                } else if (result == 2) { // 2루타
                    if (b3) { score++; b3 = false; }
                    if (b2) { score++; b2 = false; }
                    if (b1) { b3 = true; b1 = false; }
                    b2 = true; // 타자 진루
                } else if (result == 3) { // 3루타
                    if (b3) { score++; b3 = false; }
                    if (b2) { score++; b2 = false; }
                    if (b1) { score++; b1 = false; }
                    b3 = true; // 타자 진루
                } else if (result == 4) { // 홈런
                    if (b3) { score++; b3 = false; }
                    if (b2) { score++; b2 = false; }
                    if (b1) { score++; b1 = false; }
                    score++; // 타자 본인 득점
                }

                pos++;
                if (pos == 9) pos = 0;
            }
        }
        return score;
    }

    private static void permutation(int depth) {
        if (depth == 9) {
            answer = Math.max(answer, simulate());
            return;
        }

        if (depth == 3) { // 4번째 타자는 무조건 1번 선수
            permutation(depth + 1);
            return;
        }

        for (int i = 1; i < 9; i++) { // 1번 선수 제외하고 돌리기
            if (!visited[i]) {
                visited[i] = true;
                orders[depth] = i;
                permutation(depth + 1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        innings = Integer.parseInt(br.readLine());

        for (int i = 0; i < innings; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int j = 0;
            while (st.hasMoreTokens()) {
                board[j][i] = Integer.parseInt(st.nextToken());
                j++;
            }
        }

        boolean[] visited = new boolean[9];
        permutation(0);

        System.out.println(answer);
    }
}