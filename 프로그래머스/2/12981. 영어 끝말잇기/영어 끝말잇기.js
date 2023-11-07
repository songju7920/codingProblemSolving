function solution(n, words) {
    let answer = [0, 0];
    let startsWith = '';
    let turn = 1;
    let idx = 0;
    
    for(let word of words) {
        if(idx != 0 && word[0] != startsWith) {
            return [idx % n + 1, turn];
        }
        if(words.indexOf(word) != idx) {
            return [idx % n + 1, turn];
        }
        startsWith = word[word.length - 1];
        if((idx + 1) % n == 0) turn++;
        idx++;
    }

    return answer;
}