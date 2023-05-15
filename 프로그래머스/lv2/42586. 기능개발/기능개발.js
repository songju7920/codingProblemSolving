function solution(progresses, speeds) {
    let answer = [], results = [], rep = 0;
    progresses.forEach(progress => {
        results.push(Math.ceil((100-progress)/speeds[rep]));
        rep++;
    })
    while(results[0] != null){
        let Cnt = 1;
        let result = results.shift();
        while(1){
            if(result >= results[0]){ 
                results.shift();
                Cnt++;
            }
            else {
                answer.push(Cnt);
                break;
            }
        }
    }
    return answer;
}