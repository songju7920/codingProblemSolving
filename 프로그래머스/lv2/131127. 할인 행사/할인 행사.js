function solution(wants, number, discount) {
    let answer = 0;
    let totalCnt = number.reduce((a, b) => a + b);
    
    for(let i = 0; i < discount.length - totalCnt + 1; i++) {
        let cnt = 0;
        let item = discount.slice(i, 10 + i);
        wants.forEach((want, idx) => {
            let itemCnt = item.filter(a => a == want).length;
            if(number[idx] == itemCnt) cnt++;
        })
        if(cnt == wants.length) answer++;
    }
    return answer;
}