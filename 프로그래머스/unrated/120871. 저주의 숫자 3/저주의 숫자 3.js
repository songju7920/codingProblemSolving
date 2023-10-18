function solution(n) {
    let answer = 1;
    for(let i = 1; i < n; i++) {
        while(true) {
            if((answer + 1) % 3 == 0) answer++;
            else if(`${answer + 1}`.includes("3")) answer++;
            else break;
        }
        answer++;
    }
    return answer;
}