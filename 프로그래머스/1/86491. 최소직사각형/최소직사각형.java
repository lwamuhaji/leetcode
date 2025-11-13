class Solution {
    public int solution(int[][] sizes) {
        // 가로 >= 세로가 되게 돌리고 각각 최댓값 구하기
        int maxWidth = 0;
        int maxHeight = 0;
        for (int[] size : sizes) {
            int w, h;
            if (size[0] >= size[1]) {
                w = size[0];
                h = size[1];
            } else {
                w = size[1];
                h = size[0];
            }
            maxWidth = w >= maxWidth ? w : maxWidth;
            maxHeight = h >= maxHeight ? h : maxHeight;
        }
        return maxWidth * maxHeight;
    }
}