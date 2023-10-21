function solution(a, b) {
    let nums = [0, 0];
    nums[0] = Number(`${a}` + `${b}`);
    nums[1] = Number(`${b}` + `${a}`);
    return Math.max(...nums);
}