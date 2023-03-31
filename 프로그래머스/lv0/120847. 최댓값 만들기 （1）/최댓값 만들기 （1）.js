function solution(numbers) {
    var answer = 0;
    for(var i = 0; i < numbers.length - 1; i++)
        if(numbers[i] * numbers[i+1] > answer)
            answer = numbers[i] * numbers[i+1];
    return answer;
}