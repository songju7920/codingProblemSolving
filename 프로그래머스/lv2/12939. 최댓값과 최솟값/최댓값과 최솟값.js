function solution(s) {
    let numbers = s.split(' ').map(Number);
    return `${Math.min(...numbers)} ${Math.max(...numbers)}`;
}