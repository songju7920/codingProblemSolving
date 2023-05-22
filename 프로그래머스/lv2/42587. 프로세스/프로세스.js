function solution(priorities, location) {
  let answer = 0;
  let target = priorities[location];

  while (true) {
    let max = Math.max(...priorities);
    let first = priorities.shift();

    if (max === first) {
      answer++;
      if (location === 0) {
        break;
      } else {
        location--;
      }
    } else {
      priorities.push(first);
      if (location === 0) {
        location = priorities.length - 1;
      } else {
        location--;
      }
    }
  }

  return answer;
}