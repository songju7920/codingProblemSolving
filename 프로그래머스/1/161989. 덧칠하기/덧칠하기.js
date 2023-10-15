function solution(n, m, section) {
    let answer = 0;
    section.sort((a, b) => b - a);
    while(section.length > 0) {
        let start = section.pop();
        let end = start + m - 1;
        while(true) {
            if(section[section.length - 1] <= end) section.pop();
            else break;
        }
        answer++;
    }
    return answer;
}