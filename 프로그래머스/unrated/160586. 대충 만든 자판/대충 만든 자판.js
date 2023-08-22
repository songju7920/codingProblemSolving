function solution(keymap, targets) {
    var answer = [];
    targets.forEach(target => {
        let sum = 0;
        target = target.split('');
        
        //target roop
        for(let i = 0; i < target.length; i++) {
            let min = 101;
            
            //keymap 순회하면서 index 찾기
            for(let j = 0; j < keymap.length; j++){
                let idxOfKey = keymap[j].indexOf(target[i]);
                if(idxOfKey == -1) continue;
                min = idxOfKey < min ? idxOfKey : min;
            }
            
            if(min == 101) {
                sum = 0;
                break;
            } else {
                sum += min + 1;
            }
        }
        answer.push(sum == 0 ? -1 : sum);
    })
    return answer;
}