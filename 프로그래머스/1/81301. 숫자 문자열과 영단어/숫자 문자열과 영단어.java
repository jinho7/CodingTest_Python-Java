import java.util.*;

class Solution {
    public int solution(String s) {
                
        String[] temp_str = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        HashMap<String, String> num_dict = new HashMap<>();
        for (int i = 0; i < temp_str.length; i++) {
            num_dict.put(temp_str[i], Integer.toString(i));
        }
        
        // 가변 문자열 = StringBuilder 사용
        StringBuilder temp = new StringBuilder();
        StringBuilder answer = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                temp.append(c);
                if (num_dict.containsKey(temp.toString())) {
                    answer.append(num_dict.get(temp.toString()));
                    temp.setLength(0); // 초기화
                }
            }
            else {
                answer.append(c);
                temp.setLength(0); // 초기화 
            }
        }
        return Integer.parseInt(answer.toString());
    }
    
    static void print(Object o) {  
        System.out.println(o);    
    }
}
