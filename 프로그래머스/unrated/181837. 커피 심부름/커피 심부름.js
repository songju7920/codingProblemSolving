function solution(orders) {
    let answer = 0;
    orders.forEach(order => {
        if(order.includes("cafelatte")) answer += 5000;
        else answer += 4500;
    })
    return answer;
}