function solution(rsp) {
    return rsp.split('').map(hand => {return hand === "2" ? 0 : hand === "0" ? 5 : 2}).join('');
}