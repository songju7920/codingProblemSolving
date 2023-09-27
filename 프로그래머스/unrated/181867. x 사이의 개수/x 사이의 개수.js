function solution(myString) {
    var answer = [];
    let cnt = 0;
    
    myString = myString.split('x');
    myString = myString.map(char => char.length);
    answer = [...myString]
    
    return answer;
}