import java.util.*;

class Solution {
    public int bfs(ArrayList<Integer>[] adjList, int n) {
        // visited 행렬을 만들자
        boolean[] visited = new boolean[n+1];
        
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(1);
        visited[1] = true;
        int count = 0;
        
        while(!queue.isEmpty()) {
            int current = queue.remove();
            count++;
            ArrayList<Integer> adjs = adjList[current];
            for(int adj: adjs) {
                if(!visited[adj]) {
                    queue.add(adj);
                    visited[adj] = true;
                }
            }
        }
        
        return count;
    }
    
    public int solution(int n, int[][] wires) {
        int answer = n;
        
        // 인접행렬을 만들자
        boolean[][] adjMap = new boolean[n+1][n+1];
        for(int[] wire: wires) {
            adjMap[wire[0]][wire[1]] = true;
            adjMap[wire[1]][wire[0]] = true;
        }
        // 인접리스트를 만들자
        ArrayList<Integer>[] adjList = new ArrayList[n+1];
        for(int i = 1; i < n + 1; i++)
            adjList[i] = new ArrayList<>();            
        for(int[] wire: wires) {
            adjList[wire[0]].add(wire[1]);
            adjList[wire[1]].add(wire[0]);
        }
        
        for(int[] wire: wires) {
            // 간선 제거
            adjList[wire[0]].remove(Integer.valueOf(wire[1]));
            adjList[wire[1]].remove(Integer.valueOf(wire[0]));
            answer = Math.min(Math.abs(n - bfs(adjList, n) * 2), answer);
            // 간선 복구
            adjList[wire[0]].add(Integer.valueOf(wire[1]));
            adjList[wire[1]].add(Integer.valueOf(wire[0]));
        }
        
        return answer;
    }
}