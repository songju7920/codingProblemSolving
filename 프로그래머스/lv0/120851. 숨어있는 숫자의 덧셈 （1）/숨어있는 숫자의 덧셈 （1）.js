function solution(my_string) {
    var answer = 0;
    for(let i = 0; i < my_string.length; i++)
        if(isNaN(Number(my_string[i])) == false)
            answer += Number(my_string[i]);
    return answer;
}