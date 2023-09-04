function solution(s1, s2) {
    var answer = 0;
    s1.map((element) => {
        if(s2.includes(element)){
            answer++;
        }
    })
    return answer;
}