function solution(babbling) {
    let answer = babbling.filter(a => a.replaceAll(/aya|ye|woo|ma/g, "") == "");
    return answer.length
}