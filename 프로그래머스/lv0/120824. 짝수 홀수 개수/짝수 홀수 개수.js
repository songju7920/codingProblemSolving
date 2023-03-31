function solution(num_list) {
    var even = 0, odd = 0;
    for(var i = 0; i < num_list.length; i++)
    {
        if(num_list[i] % 2 == 0)
            even++
        else
            odd++
    }
    var answer = [even, odd];
    return answer;
}