function solution(num_list) {
    var answer = [];
    for(let i = 0, j = num_list.length; j != 0; i++, j--)
        answer[i] = num_list[j - 1];
    return answer;
}