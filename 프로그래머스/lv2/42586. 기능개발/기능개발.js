function solution(progresses, speeds) {
    let answer = [], Days = [], rep = 0;
    
    //개발
    progresses.forEach(progress => {
        Days.push(Math.ceil((100-progress)/speeds[rep]));
        rep++;
    })
    
    //배포
    while(Days[0] != null){
        let Cnt = 1;
        let Day = Days.shift();
        while(1){
            if(Day >= Days[0]){ 
                Days.shift();
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