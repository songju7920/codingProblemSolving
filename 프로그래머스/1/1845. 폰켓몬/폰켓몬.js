function solution(nums) {
    let types = [...new Set(nums)]
    return nums.length / 2 < types.length ? nums.length / 2 : types.length;
}