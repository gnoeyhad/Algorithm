import java.util.*;
class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        
        ArrayList<Integer> list = new ArrayList();
        
        for(int m = i; m <= j; m++){
            String m_str = m+"";
            for(int n = 0; n < m_str.length(); n++){
                list.add(m_str.charAt(n) - '0');
            }
        }

        return Collections.frequency(list, k);
    }
}