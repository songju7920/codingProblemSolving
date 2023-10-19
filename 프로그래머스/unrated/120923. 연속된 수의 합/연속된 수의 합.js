function solution(num, total) {
    let nums = new Array(num).fill(0).map((a, idx) => idx - 100);
    while(nums.reduce((a, b) => a + b) != total) nums = nums.map(a => ++a);
    return nums;
}