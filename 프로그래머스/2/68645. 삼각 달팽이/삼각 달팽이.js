function solution(n) {
    var answer = [];
    let repeat = 0;
    for(let i = 1; i <= n; i++) {
        answer.push(new Array(i).fill(0));
        repeat += i;
    }
    
    let moveLevel = 0;
    let location = [0, 0];
    let moves = [[1, 0], [0, 1], [-1, -1]];
    for(let i = 0; i < repeat; i++) {
        answer[location[0]][location[1]] = i + 1;
        
        let move = moves[moveLevel % 3];
        try {
            answer[location[0] + move[0]][location[1] + move[1]] == null
            if (answer[location[0] + move[0]][location[1] + move[1]] != 0) moveLevel++;
        } catch (err) {
            moveLevel++;
        }
        move = moves[moveLevel % 3];
        location[0] += move[0];
        location[1] += move[1];
    }
    
    return answer.reduce((a, b) => [...a, ...b]);
}