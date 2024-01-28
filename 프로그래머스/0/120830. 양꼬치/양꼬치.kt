class Solution {
    fun solution(n: Int, k: Int): Int {
        var answer: Int = (k - n / 10) * 2000 + n * 12000
        return answer
    }
}