function solution(num_list) {
    let sum = 0, multiple = 1;
    num_list.forEach(num => {
        sum += num;
        multiple *= num;
    })
    sum *= sum
    return multiple < sum ? 1 : 0;
}