function solution(num) {
    let Cnt = 0, answer = -1, compare = num;
    while(num > 1){
        if(num % 2 == 0) num /= 2;
        else {
            num *= 3; 
            num++;
        }
        if(Cnt == 500) break;
        Cnt++;
    }
    return compare == 1 ? 0 : Cnt == 500 ? -1 : Cnt;
}