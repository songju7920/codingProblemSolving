function solution(prices) {
    let answer = new Array(prices.length).fill(0);
    let length = prices.length;
    
    for(let i = 0; i < length; i++) {
        for(let j = i + 1; j < length; j++) {
            answer[i]++;
            if(!(prices[i] <= prices[j])) break;
        }
    }
    
    return answer;
}