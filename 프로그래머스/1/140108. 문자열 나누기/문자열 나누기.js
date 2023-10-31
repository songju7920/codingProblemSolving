function solution(s) {
    var answer = 0;
    let idx = 0;
    while(s.length > idx) {
        let same = 0;
        let diff = 0;
        let target = s[idx];
        for(let i = idx; i < s.length; i++) {
            if(s[i] == target) same++;
            else diff++;
            idx++;
            if(same == diff) break;
        }
        answer++;
    }
    return answer;
}