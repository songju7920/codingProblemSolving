function solution(n) {
    var answer = 1;
    for(;;answer++)
        if(6 * answer % n == 0)
            break;
    return answer;
}