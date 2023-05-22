function solution(k, m, score) {
    var answer = 0;
    score.sort();
    while(score.length >= m){
        let basket = [];
        while(basket.length != m) basket.push(score.pop());
        answer += basket.pop() * m;
    }
    
    return answer;
}