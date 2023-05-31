function solution(number, k) {
    let answer = [];
    number = number.split('').reverse();
    
    if(k == 1) number.shift();
    
    while(number.length > 0) {
        answer.push(number.pop());
        while(answer[answer.length - 1] < number[number.length - 1] && k > 0) {
            answer.pop();
            k -= 1;
        }
    }
    
    return answer.join('');
}
