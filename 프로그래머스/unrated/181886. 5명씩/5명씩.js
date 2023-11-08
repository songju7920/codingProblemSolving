function solution(names) {
    var answer = [];
    let length = names.length;
    for(let i = 0; i < length; i += 5) answer.push(names[i]);
    return answer;
}