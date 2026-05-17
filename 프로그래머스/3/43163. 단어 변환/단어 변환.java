import java.util.*;

class Solution {
    
    private boolean canChange(String a, String b) {
        char[] arrA = a.toCharArray();
        char[] arrB = b.toCharArray();
        int diff = 0;
        for(int i = 0; i < a.length(); i++) {
            if (arrA[i] != arrB[i]) diff++;
        }
        return diff == 1;
    }
    
    public int solution(String begin, String target, String[] words) {
        Queue<String> queue = new ArrayDeque<>();
        queue.add(begin);
        
        Map<String, Integer> visited = new HashMap<>();
        visited.put(begin, 0);
        
        while(!queue.isEmpty()) {
            String current = queue.poll();
            
            if(current.equals(target)) {
                return visited.get(target);
            }
            
            for(String word: words) {
                if(!visited.containsKey(word) && canChange(current, word)) {
                    queue.add(word);
                    visited.put(word, visited.get(current) + 1);
                }
            }
        }
        
        return 0;
    }
}