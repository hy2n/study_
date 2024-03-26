class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String ans_1 = Integer.toString(a) + Integer.toString(b);
        String ans_2 = Integer.toString(b) + Integer.toString(a);
        
        if (Integer.parseInt(ans_1)>Integer.parseInt(ans_2)) return Integer.parseInt(ans_1);
        else return Integer.parseInt(ans_2);
    }
}