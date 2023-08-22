function solution(keymap, targets) {
    var answer = [];
    targets.forEach(target => {
        let sum = 0;
        target = target.split('');
        
        for(let i = 0; i < target.length; i++) {
            let min = 101;
            for(let j = 0; j < keymap.length; j++){
                let idxOfKey = keymap[j].indexOf(target[i]);
                if(idxOfKey == -1) continue;
                min = idxOfKey < min ? idxOfKey : min
            }
            
            if(min == 101) {
                sum = 0;
                break
            }
            sum += min + 1;
        }
        
        if(sum == 0){
            answer.push(-1);
        } else {
            answer.push(sum);
        }
    })
    return answer;
}