function solution(dartResult) {
    let scores = [];
    let option;
    
    //데이터 분리
    let dartData = dartResult.match(/(\d+)|([A-Z]+)|(\W+)/g);
    while(dartData.length > 0){
        let score = dartData.shift();
        let bonus = dartData.shift();
        if(dartData[0] == '*' || dartData[0] == '#')
            option = dartData.shift();
        else
            option = null;
        
        //점수 제곱
        switch(bonus){
            case 'S':
                scores.push(Number(score));
                break;
            case 'D':
                scores.push(score*score);
                break;
            case 'T':
                scores.push(score*score*score);
                break;
        }
        
        //옵션처리
        switch(option){
            case '*':
                if(scores.length > 1){
                     let a = scores.pop() * 2;
                     scores.push(scores.pop() * 2);
                     scores.push(a);
                }
                else scores[0] *= 2
                break;
            case '#':
                scores.push(scores.pop() * -1);
                break;
            case null:
                break;
        }
    }
    
    return scores.reduce((a, b) => (a + b));
}