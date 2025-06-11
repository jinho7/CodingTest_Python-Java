import java.util.*;

class Solution {
    public long solution(long n) {
        // 1. 문자열로 변환
        String s = String.valueOf(n);
        // 2. char로 변환시켜서 char[]에 담아주기
        char[] ch = s.toCharArray();
        // 3. 내림차순 정렬 위해서 다시 Character[] (Wrapper Type)으로 바꿔줘야 함..
        Character[] arr = new Character[ch.length];
        for (int i = 0; i < ch.length; i++) {
            arr[i] = ch[i];
        }
            
        // // 3. 이것도 가능함! char[] → List<Character>
        // List<Character> list = new ArrayList<>();
        // for (char c : chars) {
        //     list.add(c); // autoboxing 발생
        // }
        
        // 4. 실제 정렬
        Arrays.sort(arr, (a, b) -> b - a);
        
        // 5. 다시 String으로 변환
        StringBuilder sb = new StringBuilder();
        for (char c : arr) {
            sb.append(c);
        }
        
        long answer = Long.parseLong(sb.toString());
        return answer;
    }
}