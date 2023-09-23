function solution(n, control) {
    control.split('').map(a => {
        if(a == 'w') n++;
        if(a == 's') n--;
        if(a == 'd') n += 10;
        if(a == 'a') n -= 10;
    })
    return n;
}