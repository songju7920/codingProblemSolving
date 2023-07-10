function solution(s) {
    let result = [];
    let idx = 0;
    s = s.split("");
    
    s.forEach((char) => {
        if(char == " "){
            result.push(" ");
            idx = 0;
            return 0;
        }else if(!(idx % 2)){
            result.push(char.toUpperCase());
        }else{
            result.push(char.toLowerCase());
        }
        idx++;
    })
    
    return result.reduce((a, b) => a + b);
}