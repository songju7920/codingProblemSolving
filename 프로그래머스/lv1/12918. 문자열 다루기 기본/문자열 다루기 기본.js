function solution(s) {
    var answer = false;
    if(s.length == 4 || s.length == 6){
        if(s.indexOf("e") != -1) answer = false;
        else if(!isNaN(Number(s))) answer = true;
    }
    return answer;
}