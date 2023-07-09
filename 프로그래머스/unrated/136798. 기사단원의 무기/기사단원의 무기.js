function solution(number, limit, power) {
    let powers = [];
    
    while(number != 0){
        let cnt = 0;
        for(let i = 1; i <= Math.pow(number ,0.5); i++){
            if(number % i == 0){
                cnt++;
			    if (i != number / i) cnt++;
            }
        }
        
        //제한넘으면 지정 공격력으로 바꾸기
        if(cnt > limit) cnt = power;
        powers.push(cnt);
        number--;
    }
    
    console.log(powers);
    let answer = powers.reduce((a, b) => a + b)
    return answer;
}