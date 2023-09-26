function solution(targets) {
    targets = targets.sort((a, b) => b[0] - a[0]);
    let points = targets.map(a => a[0]);
    let CurrentPoint = points[0] + 0.1;
    let answer = 1;
    
    for(let i = 1; i < targets.length; i++) {
        if(!(targets[i][0] < CurrentPoint && targets[i][1] > CurrentPoint)) {
            CurrentPoint = points[i] + 0.1;
            answer++;
        }
    }
    
    return answer;
}