function solution(s) {
    let answer = [0, 0];
    while(s.length > 1){
        s = s.split('');
        
        let length = s.length;
        
        for(let i = 0; i < length; i++){
            let num = s.shift();
            if(num == "1"){
                s.push(num);
            } else {
                answer[1]++;
            }
        }
        
        
        answer[0]++;
        s = s.length.toString(2);
    }
    
    return answer;
}