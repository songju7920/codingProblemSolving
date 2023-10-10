function solution(answers) {
    let guesses = [[1, 2, 3, 4, 5], 
                   [2, 1, 2, 3, 2, 4, 2, 5], 
                   [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]];
    let length = answers.length;
    let correctCnt = [0, 0, 0];
    let result = [];
    
    for(let i = 0; i < length; i++) {
        let answer = answers[i];
        if(guesses[0][i % 5] == answer) correctCnt[0]++;
        if(guesses[1][i % 8] == answer) correctCnt[1]++;
        if(guesses[2][i % 10] == answer) correctCnt[2]++;
    }
    
    let max = Math.max(...correctCnt);
    return correctCnt
        .map((a, idx) => {if(a == max) return idx + 1})
        .filter(a => a != null);
}