function solution(lottos, win_nums) {
    let least = 7, max = 7;
    
    lottos.map(lottoNum => {
        if(lottoNum == 0){
            max--;
        } else if(win_nums.indexOf(lottoNum) != -1) {
            max--;
            least--;
        }
    });
    
    if(max == 7) max--;
    if(least == 7) least--;
    
    return [max, least];
}