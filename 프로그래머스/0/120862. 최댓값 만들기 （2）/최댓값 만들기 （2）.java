import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer_1 = 0;
        int answer_2 = 0;
       
        ArrayList<Integer> list = new ArrayList();
        
        for(int i = 0 ; i < numbers.length; i++){
            list.add(numbers[i]);
        }
        
        Collections.sort(list);
        
        
        answer_1 = list.get(0)*list.get(1);
        answer_2 = list.get(list.size()-1)*list.get(list.size()-2);
        
        return Math.max(answer_1, answer_2);

    }
}