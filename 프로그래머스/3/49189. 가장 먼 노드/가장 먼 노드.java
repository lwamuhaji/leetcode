import java.util.*;

class Solution {

    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        // 인접리스트를 만들자
        List<List<Integer>> adjList = new ArrayList<>();
        for(int i = 0; i < n+1; i++) {
            adjList.add(new ArrayList<Integer>());
        }
        for(int[] e: edge) {
            adjList.get(e[0]).add(e[1]);
            adjList.get(e[1]).add(e[0]);
        }
        
        // visited, d, pq 초기화
        boolean[] visited = new boolean[n+1]; visited[1] = true;
        int[] d = new int[n+1]; Arrays.fill(d, 50000); d[0] = 0; d[1] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]); pq.add(new int[] {1, 0});

        // 다익스트라
        while(!pq.isEmpty()) {
            int[] current = pq.remove();    
            visited[current[0]] = true;
            
            if(current[1] > d[current[0]]) continue;
            
            // d 갱신
            for(int idx: adjList.get(current[0])) {
                if(d[idx] > current[1] + 1) {
                    d[idx] = Math.min(d[idx], current[1] + 1);
                    pq.add(new int[] {idx, d[idx]});
                }
            }
        }
        
        int max = Arrays.stream(d).max().getAsInt();
        for(int i = 1; i < n+1; i++) {
            if(max == d[i]) answer++;
        }
        
        return answer;
    }
}