function solution(s) {
    let answer = [-1];
    let len = s.length;
    
    for(let i = 1; i < len; i++) {
        let str = s.slice(0, i);
        let idx = str.lastIndexOf(s[i]);
        answer.push(idx == -1 ? idx : i - idx)
    }
    
    return answer;
}