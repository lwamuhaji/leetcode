import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        if (!st.hasMoreTokens()) return; // 방어 코드
        
        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[] timeline = new int[n * w + w + 100]; 
        
        int t = 1;
        int count = 0; // 처리한 트럭 수
        
        st = new StringTokenizer(""); 
        
        while(count < n) {
            while (!st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) break;
                st = new StringTokenizer(line);
            }
            
            int currentTruckWeight = Integer.parseInt(st.nextToken());
            
            while (true) {
                if (timeline[t] + currentTruckWeight <= L) {
                    for (int i = 0; i < w; i++) {
                        timeline[t + i] += currentTruckWeight;
                    }
                    t++; 
                    count++;
                    break; 
                } else {
          
                    t++;
                }
            }
        }
        
        System.out.println((t - 1) + w);
    }
}