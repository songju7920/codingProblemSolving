function solution(num_list) {
    let answer;
    if(num_list.length <= 10) answer = 1;
    else answer = 0;
    num_list.forEach(num => {
        if(num_list.length <= 10) answer *= num;
        else answer += num;
    })
    return answer;
}