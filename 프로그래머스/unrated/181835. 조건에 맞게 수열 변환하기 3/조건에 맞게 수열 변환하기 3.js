function solution(arr, k) {
    var answer = [];
    let cnt = 0;
    arr.forEach(element => {
        if(k % 2 == 0) answer[cnt] = element + k;
        else answer[cnt] = element * k
        cnt++;
    })
    return answer;
}