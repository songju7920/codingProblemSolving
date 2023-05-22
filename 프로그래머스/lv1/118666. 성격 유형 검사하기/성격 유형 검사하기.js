function solution(survey, choices) {
    let answer = "";
    const MBTI = {
        'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0
    }
    
    //MBTI 데이터 수집
    survey.forEach((surveyType,idx)=>{
        const [front,back] = surveyType.split('')

        if(choices[idx] < 4) MBTI[front] += Math.abs(choices[idx]-4)
        else if(choices[idx] > 4) MBTI[back] += Math.abs(choices[idx]-4)
    })
    
    //MBTI 결정
    answer = answer.concat(MBTI['R'] >= MBTI['T'] ? 'R' : 'T')
    answer = answer.concat(MBTI['C'] >= MBTI['F'] ? 'C' : 'F')
    answer = answer.concat(MBTI['J'] >= MBTI['M'] ? 'J' : 'M')
    answer = answer.concat(MBTI['A'] >= MBTI['N'] ? 'A' : 'N')
    
    return answer;
}