// 소수 확인 함수
const chackPrime = (num) => {
    let result = true;
    for(let k = 2; k <= Math.floor(num / 2); k++) {
        if(num % k == 0) {
            result = false;
            break;
        }
    }
    return result;
}

function solution(nums) {
    let answer = 0;
    let len = nums.length;
    
    for(let i = 0; i < len - 2; i++) {
        for(let j = i + 1; j < len - 1; j++) {
            for(let k = j + 1; k < len; k++) {
                let num = nums[i] + nums[j] + nums[k];
                let isPrime = chackPrime(num);
                if(isPrime) answer++;
            }
        }
    }
    
    return answer;
}