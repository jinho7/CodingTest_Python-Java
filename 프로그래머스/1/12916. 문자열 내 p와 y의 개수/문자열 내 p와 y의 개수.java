class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        int[] arr = new int[2];
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'p') {
                arr[0] += 1;
            }
            else if (c == 'y') {
                arr[1] += 1;
            }
        }
        
        return (arr[0] == arr[1] ? true : false);
    }
}