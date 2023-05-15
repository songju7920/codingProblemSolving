function solution(progresses, speeds) {
    let answer = [], results = [], rep = 0;
    
    //개발
    progresses.forEach(progress => {
        results.push(Math.ceil((100-progress)/speeds[rep]));
        rep++;
    })
    
    //배포
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