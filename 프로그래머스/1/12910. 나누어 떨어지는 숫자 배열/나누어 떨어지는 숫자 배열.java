import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> answer = new ArrayList<>();

        Arrays.sort(arr);
        for (int x: arr) {
            if (x % divisor == 0) {
                answer.add(x);
            }
        }
        
        return (!answer.isEmpty()) ? answer.stream().mapToInt(i -> i).toArray() : new int[]{-1};
    }
}