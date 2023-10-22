function solution(array) {
    var answer = Math.max(...array);
    return [answer, array.indexOf(answer)];
}