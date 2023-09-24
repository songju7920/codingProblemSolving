function solution(n) {
    var answer = [];
    answer.push(n);
    while(n != 1) {
        if(n % 2 == 0) {
            n /= 2;
            answer.push(n);
        } else {
            n *= 3;
            n++;
            answer.push(n);
        }
    }
    return answer;
}