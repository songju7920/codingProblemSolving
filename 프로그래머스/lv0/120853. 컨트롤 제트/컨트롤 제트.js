function solution(s) {
    let sum = 0, savedNum = 0;
    const numbers = s.split(" ");
    numbers.forEach(num =>{
        if(num == 'Z'){
            sum -= savedNum;
            console.log(sum);
        }
        else if(num != ' '){
            sum += Number(num);
            savedNum = Number(num);
            console.log(sum);
        }
    })
    return sum;
}