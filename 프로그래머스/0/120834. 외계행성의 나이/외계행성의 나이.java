class Solution {
    public String solution(int age) {
        String answer = "";
        for (String str : Integer.toString(age).split("")) {
            answer += (char)(Integer.parseInt(str) + 97);
        }
        return answer;
    }
}