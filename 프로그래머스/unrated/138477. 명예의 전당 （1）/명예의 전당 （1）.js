function solution(k, scores) {
    let ranking = [];
    let answer = [];
    
    scores.forEach((score) => {
        if(ranking.length < k){
            ranking.push(score);
        }
        else if(ranking.length >= k && score > Math.min(...ranking)){
            let location = ranking.indexOf(Math.min(...ranking));
            ranking.splice(location, 1);
            ranking.push(score);
        }
        
        //정답 배열에 최소값 넣기
        answer.push(Math.min(...ranking));
    })
    
    return answer;
}