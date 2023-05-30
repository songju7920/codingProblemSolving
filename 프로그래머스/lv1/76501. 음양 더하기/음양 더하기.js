function solution(absolutes, signs) {
    let answer = 0;
    absolutes.forEach((absolute, idx) => {
        answer += signs[idx] == 1 ? absolute : -absolute;
    })
    return answer;
}