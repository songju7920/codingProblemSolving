function solution(x) {
    let X = (String(x)).split(''), sum = 0;
    for(let i = 0; i < X.length; i++) sum += Number(X[i])
    console.log(sum)
    return x % sum === 0;
}