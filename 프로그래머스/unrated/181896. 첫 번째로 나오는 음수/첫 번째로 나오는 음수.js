function solution(num_list) {
    return num_list.indexOf(num_list.filter(a => a < 0)[0]);
}