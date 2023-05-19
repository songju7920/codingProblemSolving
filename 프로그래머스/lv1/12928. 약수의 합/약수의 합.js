function solution(n) {
    let sum = n;
    for(let i = 1; i <= n/2; i++)
        if(n % i == 0)
            sum += i;
    return sum;
}