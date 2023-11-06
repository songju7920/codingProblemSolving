function solution(brown, yellow) {
    var answer = [];
    let lengths = [];
    let size = brown + yellow;
    
    for(let i = 3; i <= size / 2; i++) {
        if(size % i == 0 && size / i >= i) {
            lengths.push([size / i, i]);
        }
    }
    
    for(let length of lengths) {
        if((length[0] + length[1] - 2) * 2 == brown) {
            answer = length;
            break;
        }
    }
    
    return answer;
}