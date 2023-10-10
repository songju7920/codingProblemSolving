function solution(n, t, m, p) {
    let answer = '';
    let numArr = [];
    
    let i = 0;
    while(m * t > numArr.length) {
        numArr.push(...i.toString(n).split(''));
        i++
    }
    
    for(let i = 0; i < t * m; i += m) {
        answer += numArr[p + i - 1]
    }
    
    return answer.toUpperCase();
}