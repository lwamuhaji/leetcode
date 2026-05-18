import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int H = triangle.length;
        
        int[][] new_tri = new int[H][];
        for(int i = 0; i < H; i++) {
            new_tri[i] = new int[triangle[i].length];
        }
        new_tri[0][0] = triangle[0][0];
        
        for(int i = 0; i < H-1; i++) {
            for(int j = 0; j < triangle[i].length; j++) {
                new_tri[i+1][j] = Math.max(new_tri[i+1][j], triangle[i+1][j] + new_tri[i][j]);
                new_tri[i+1][j+1] = Math.max(new_tri[i+1][j+1], triangle[i+1][j+1] + new_tri[i][j]);
            }
        }
        
        return Arrays.stream(new_tri[H-1]).max().getAsInt();
    }
}