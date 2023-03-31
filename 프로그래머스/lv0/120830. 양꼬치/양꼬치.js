function solution(n, k) {
    var answer = 0;
    if(n > 9)
        for(var i = n; 9 < i; i -= 10)
            k--;
    return 12000 * n + 2000 * k;
}