function solution(d, budget) {
    let answer = 0, Cnt = 0;
    d.sort((a, b) => a - b)
    console.log(d);
    d.forEach(budgetReq => {
        if(answer + budgetReq > budget) return 0;
        answer += budgetReq;
        Cnt++;
    })
    return Cnt;
}