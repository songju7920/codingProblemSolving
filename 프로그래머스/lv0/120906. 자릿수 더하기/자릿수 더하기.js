function solution(n) {
    let answer = 0;
    let div = 10;
    
    while(div <= n * 10){
        answer += n % div / (div / 10);
        n -= n % div;
        div *= 10;
    }
    
    return answer;
}