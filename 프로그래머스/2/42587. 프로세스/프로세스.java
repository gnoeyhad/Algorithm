import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        // 우선순위가 높은 숫자 순 priority queue 선언
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        
        // 우선순위 큐에 프로세스 우선순위 추가 
        for(int p : priorities){
            priorityQueue.add(p);
        }
        
        while(!priorityQueue.isEmpty()){
            // 기존 우선순위 배열 순회
            for(int i = 0; i < priorities.length; i++){
                // 현재 작업의 위치 찾기
                if(priorities[i] == priorityQueue.peek()){
                    priorityQueue.poll(); // priorityQueue의 첫번째 값을 반환하고 제거
                    answer++; // 프로세스를 꺼낸 개수를 count 
                    
                    // 현재 작업이 주어진 location과 같다면
                    if(i == location){
                        return answer; // 지금까지 꺼낸 프로세스의 수를 반환
                    }
                }
            }
        }
        
        return answer;
    }
}