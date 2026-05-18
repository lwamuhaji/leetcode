import java.util.*;

class Solution {
    int[][] D = {{0,1},{1,0},{-1,0},{0,-1}};
    
    public int solution(int[][] maps) {
        int answer = 0;
        int H = maps.length;
        int W = maps[0].length;
        
        Queue<int[]> q = new ArrayDeque<>();
        int[][] visited = new int[H][W];
        
        q.add(new int[] {0, 0});
        visited[0][0] = 1;
        
        while(!q.isEmpty()) {
            int[] current = q.poll();
            int cx = current[0], cy = current[1];
            
            for(int[] d: D) {
                int nx = cx + d[0], ny = cy + d[1];
                if(0 <= nx && nx < H && 0 <= ny && ny < W && visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                    q.add(new int[] {nx, ny});
                    visited[nx][ny] = visited[cx][cy] + 1;
                }
            }
        }
        
        return visited[H-1][W-1] == 0 ? -1 : visited[H-1][W-1];
    }
}