const slice = (str, num) => {
    let result = [];
    let len = str.length;
    for(let i = num; i <= len; i++){
        result.push(str.slice(i-num, i));
    }
    return result.map(a => Number(a));
}

function solution(t, p) {
    let num = Number(p);
    let answer = slice(t, p.length).filter(a => a <= num).length;
    return answer;
}