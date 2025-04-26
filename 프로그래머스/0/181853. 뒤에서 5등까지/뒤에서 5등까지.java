import java.util.*;

class Solution {
    public List<Integer> solution(int[] num_list) {
        // 1. 정렬
        Arrays.sort(num_list);

        // 2. 앞에서 5개만 리스트에 담기
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            answer.add(num_list[i]);
        }

        return answer;
    }
}
