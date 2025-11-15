import java.util.*;

class Solution {
    
    static class Node {
        public int play;
        public int id;
        
        Node(int play, int id) {
            this.play = play;
            this.id = id;
        }
        
        public int compareTo(Node n) {
            if(n.play > this.play) {
                return 1;
            } else if (n.play < this.play) {
                return -1;
            } else if (n.play == this.play && n.id < this.id) {
                return 1;
            } else {
                return -1;
            }
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        
        // 각 장르별 재생 횟수 세기 O(n)
        // 동시에 장르별 곡 id 기록
        HashMap<String, Integer> hm = new HashMap<>();
        HashMap<String, List<Integer>> genreAndIds = new HashMap<>();
        for(int i = 0; i < genres.length; i++) {
            if(!Objects.isNull(hm.get(genres[i]))) {
                hm.put(genres[i], hm.get(genres[i]) + plays[i]);
            } else {
                hm.put(genres[i], plays[i]);
            }
            
            if(Objects.isNull(genreAndIds.get(genres[i]))) {
                genreAndIds.put(genres[i], new ArrayList<>(Arrays.asList(i)));
            } else {
                genreAndIds.get(genres[i]).add(i);
            }
        }
        
        // 장르 정렬 O(nlogn)
        ArrayList<Map.Entry<String, Integer>> arr = new ArrayList<>(hm.entrySet());
        Collections.sort(arr, Map.Entry.comparingByValue(Comparator.reverseOrder()));

        // 각 장르 내 노래 정렬 (재생 횟수[내림], 고유번호[오름]) O(nlogn)
        HashMap<String, List<Node>> hmm = new HashMap<>();
        for(var e: arr) {
            if(!hmm.containsKey(e.getKey())) {
                List<Node> rank = new ArrayList<>();
                rank.add(new Node(-1, -1));
                rank.add(new Node(-1, -1));
                hmm.put(e.getKey(), rank);
            }
            for(int id: genreAndIds.get(e.getKey())) {
                Node node = new Node(plays[id] ,id);
                
                List<Node> rank = hmm.get(e.getKey());
                if(rank.get(0).compareTo(node) == 1) {
                    rank.set(1, rank.get(0));
                    rank.set(0, node);
                } else if(rank.get(1).compareTo(node) == 1) {
                    rank.set(1, node);
                }
            }
            
            for(var node: hmm.get(e.getKey())) {
                if (node.id > -1)
                    answer.add(node.id);
            }
        }
        
        
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
