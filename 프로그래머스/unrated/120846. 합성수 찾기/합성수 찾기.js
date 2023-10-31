function solution(n) {
    var answer = 0;
    for(let i = 2; i <= n; i++) {
        for(let j = 2; j <= i / 2; j++) {
            if(i % j == 0) {
                answer++;
                break;
            }
        }
    }
    return answer;
}