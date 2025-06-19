class Solution {
    public int solution(int num) {
        int count = 0;
        Long x = (long) num;
        while (x != 1) {
            count += 1;
            if (count == 500) {
                return -1;
            }
            // 짝수
            if (x % 2 == 0) {
                x /= 2;
            }

            // 홀수
            else {
                x = (x * 3) + 1;
            }
        }
        return count;
    }
}