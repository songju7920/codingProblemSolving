function solution(n, m) {
    let nums = [n, m].sort((a, b) => a - b);
    let answer = [nums[0], 0];
    
    // 최대공약수
    for(let i = nums[0];; i--) {
        if(nums[0] % i == 0 && nums[1] % i == 0) break;
        if(answer[0] == 1) break;
        answer[0]--;
    }
    
    // 최소공배수
    for(let i = nums[1];; i += nums[1]) 
        if(i % nums[0] == 0) {
            answer[1] = i;
            break;
        };
    
    return answer;
}