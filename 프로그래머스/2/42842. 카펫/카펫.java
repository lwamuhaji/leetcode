class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        // brown + yellow = answer[0] * answer[1]
        // 모든 answer 조합을 검사한다. (가로 세로 최솟값 = 3)
        // answer 쌍이 정해지면 yellow의 width와 height이 정해진다. -> width*height=yellow
        int sum = brown + yellow;
        for(int w = 3; w <= sum/3; w++){
            if(sum%w==0) {
                int h = sum/w;
                int width = w - 2;
                int height = h - 2;
                if (width * height == yellow){
                    answer[0] = w;
                    answer[1] = h;
                }
            }
        }
        
        return answer;
    }
}