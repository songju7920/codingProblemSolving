class Solution {
    fun solution(numbers: IntArray): Double {
        var answer: Double = numbers.sum().toDouble() / numbers.size
        return answer
    }
}