import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int x : arr) {
            list.add(x);
        }
        int min = Collections.min(list);
        list.remove(Integer.valueOf(min));
        
        // int[] answer = list.stream()
        //         .mapToInt(Integer::intValue)
        //         .toArray();
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer.length > 0 ? answer : new int[]{-1};
    }
}