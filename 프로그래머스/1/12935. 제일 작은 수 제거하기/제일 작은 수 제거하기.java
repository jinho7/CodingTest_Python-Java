import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            list.add(arr[i]);
        }
        int min = Collections.min(list);
        list.remove(Integer.valueOf(min));
        
        int[] answer = list.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        return answer.length > 0 ? answer : new int[]{-1};
    }
}