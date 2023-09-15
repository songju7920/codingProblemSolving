function solution(N, stages) {
    let failureRates = [];
    let answer = [];
    let players = stages.length;
    
    for(let i = 1; i <= N; i++){
        answer.push(i);
    }
    
    for(let i = 1; i <= N; i++){
        let leftPlayers = stages.filter(stage => stage == i).length;
        failureRates.push(leftPlayers / players);
        players -= leftPlayers;
    }
    
    answer.sort((a, b) => {
        let idxA = answer.indexOf(a);
        let idxB = answer.indexOf(b);
        
        return failureRates[idxB] - failureRates[idxA];
    })
    
    return answer;
}