function solution(queue1, queue2) {
    let answer = 0;
    let sum1 = queue1.reduce((a, b) => a + b);
    let sum2 = queue2.reduce((a, b) => a + b);
    let start1 = 0;
    let start2 = 0;
    
    while(sum1 !== sum2) {
        if(sum1 > sum2) {
            let num = queue1[start1];
            queue2.push(num);
            sum1 -= num;
            sum2 += num;
            start1++;
        } else {
            let num = queue2[start2];
            queue1.push(num);
            sum2 -= num;
            sum1 += num;
            start2++;
        }
        
        if(queue1.length > 1000000 || queue2.length > 1000000) return -1;
        answer++;
    }
    
    return answer;
}