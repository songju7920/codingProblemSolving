function solution(s){
    let stack = [];
    s = s.split('');
        
    for (let char of s) {
        if(char == ')' && stack.length == 0) return false
        if(char == '(') stack.push(char);
        if(char == ')') stack.pop();
    }
    
    return stack.length == 0;
}