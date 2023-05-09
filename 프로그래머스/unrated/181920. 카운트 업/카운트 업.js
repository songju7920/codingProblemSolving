function solution(start, end) {
    var answer = [];
    for(let i = 0; i < end - start + 1; i++){
        answer[i] = start+i;
    }
    return answer;
}