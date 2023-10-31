function solution(numbers, k) {
    let location = 0;
    let length = numbers.length;
    for(let i = 0; i < k - 1; i++) {
        location = (location + 2) % length;
    }
    return numbers[location];
}