function solution(s, n) {
    let answer = [];
    s = s.split('');
    
    for(let c of s) {
        if(c == ' ') {
            answer.push(' ');
            continue;
        }
        
        let Ascii = c.charCodeAt();
        if(Ascii < 91) {
            Ascii += n;
            if(Ascii > 90) answer.push(String.fromCharCode(64 + Ascii % 90));
            else answer.push(String.fromCharCode(Ascii));
        }
        else if(96 < Ascii) {
            Ascii += n;
            if(Ascii > 122) answer.push(String.fromCharCode(96 + Ascii % 122));
            else answer.push(String.fromCharCode(Ascii));
        }
    }
    
    return answer.join('');
}