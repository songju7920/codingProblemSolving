function solution(s, n) {
    let lowers = 'abcdefghijklmnopqrstuvwxyz';
    let uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let answer = '';
    
    for(let char of s) {
        // 공백 처리
        if(char == ' ') answer += ' ';
        
        // 대문자 변환
        else if(char.toUpperCase() == char) {
            let idx = uppers.indexOf(char) + n;
            answer += uppers[idx % 26];
        }
        
        // 소문자 변환
        else {
            let idx = lowers.indexOf(char) + n;
            answer += lowers[idx % 26];
        }
    }
    return answer;
}