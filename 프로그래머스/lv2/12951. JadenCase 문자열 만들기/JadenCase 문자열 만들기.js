function solution(s) {
    let words = s.split('');
    words[0] = words[0].toUpperCase();
    
    for (let i = 1; i < words.length; i++) {
        if(words[i] === ' '){
            if(words[i+1] != ' ' && words[i+1] != undefined){
                words[i+1] = words[i+1].toUpperCase();
                i++;
            }
            continue;
        }
        
        words[i] = words[i].toLowerCase();
    }
    return words.join('');
}