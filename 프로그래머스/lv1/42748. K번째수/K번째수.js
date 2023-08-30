function solution(array, commands) {
    let answer = [];
    commands.map((commend) => {
        let start = commend[0] - 1;
        let end = commend[1];
        let target = commend[2] - 1;
        answer.push(array.slice(start, end).sort((a, b) => a - b)[target])
    })
    return answer;
}