import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        // 각 패턴
        int[][] pattern = {{1,2,3,4,5}, {2,1,2,3,2,4,2,5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        int[] count = {0, 0, 0};

        for(int i = 0; i < answers.length; i++) {
            for(int j = 0; j < 3; j++) {
                if (answers[i] == pattern[j][i%pattern[j].length]) {
                    count[j]++;
                }
            }
        }
        
        List<Integer> answer = new ArrayList<>();
        int max = Arrays.stream(count).max().getAsInt();
        for(int i = 0; i < 3; i++) {
            if (max == count[i]) answer.add(i+1);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}