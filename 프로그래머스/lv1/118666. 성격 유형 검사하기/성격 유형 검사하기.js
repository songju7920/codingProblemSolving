//MBTI 데이터
const MBTI = {
    R: 0, T: 0,
    C: 0, F: 0,
    J: 0, M: 0,
    A: 0, N: 0,
}
    
function solution(survey, choices) {
    var answer = '';
    
    //MBTI 데이터 분류
    choices.forEach((choice, idx) => {
        if(4 > choice) {
            MBTI[survey[idx].split("")[0]] += 4 - choice;
        } else if(4 < choice) {
            MBTI[survey[idx].split("")[1]] += choice - 4;
        }
    })
    
    //MBTI 결정
    answer += MBTI.R < MBTI.T ? "T" : "R"
    answer += MBTI.C < MBTI.F ? "F" : "C"
    answer += MBTI.J < MBTI.M ? "M" : "J"
    answer += MBTI.A < MBTI.N ? "N" : "A"
    
    return answer
}