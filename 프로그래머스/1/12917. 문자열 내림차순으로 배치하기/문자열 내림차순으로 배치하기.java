import java.util.*;

class Solution {
    public String solution(String s) {
        // 문자열 역순 정렬, 소문자 > 대문자
        List<Character> charList = new ArrayList<>();
        for (char x :s.toCharArray()) {
            charList.add(x);
        }
        charList.sort(Comparator.reverseOrder());
        StringBuilder answer = new StringBuilder();
        for (char x :charList) {
            answer.append(x);
        }
        return answer.toString();
    }
}