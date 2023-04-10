function solution(money) {
    var answer = [];
    answer[0] = ~~(money / 5500);
    answer[1] = money % 5500;
    return answer;
}