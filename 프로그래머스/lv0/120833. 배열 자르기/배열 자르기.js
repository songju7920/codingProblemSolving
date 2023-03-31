function solution(numbers, num1, num2) {
    var answer = [];
    for(var i = 0; num1 <= num2; i++, num1++)
        {
            answer[i] = numbers[num1];
        }
    return answer;
}