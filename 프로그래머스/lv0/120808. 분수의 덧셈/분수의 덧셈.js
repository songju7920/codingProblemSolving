function solution(numer1, denom1, numer2, denom2) {
    let topNum = numer1 * denom2 + numer2 * denom1;
    let bottomNum = denom1 * denom2;
    let max = 1;
    for(let i = 1; i <= bottomNum; i++)
        {
            if(topNum % i == 0 && bottomNum % i == 0)
               max = i;
        }
    return [topNum/max, bottomNum/max];
}