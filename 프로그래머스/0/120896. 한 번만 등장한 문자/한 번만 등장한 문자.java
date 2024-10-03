import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        
        ArrayList<Character> list = new ArrayList(); 
        
        for(int i = 0; i<s.length(); i++){
            list.add(s.charAt(i));
        }
        
        Collections.sort(list);
        
        for(int i = 0; i<list.size(); i++){
            if(Collections.frequency(list, list.get(i))==1){
                answer += list.get(i);
            }
        }
        
        System.out.println(answer);
        
        return answer;
    }
}