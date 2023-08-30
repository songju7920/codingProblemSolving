function solution(array, commands) {
    let answer = [];
    commands.map((commend) => {
        let [start, end, target] = commend;
        answer.push(array.slice(start - 1, end).sort((a, b) => a - b)[target - 1])
    })
    return answer;
}