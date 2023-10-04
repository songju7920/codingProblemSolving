function solution(people, limit) {
    let answer = 0;
    people = people.sort((a, b) => a - b)
    
    while (people.length > 0) {
        if(people[0] + people[people.length - 1] <= limit && people.length > 1) {
            people.pop();
            people.shift();
            answer++;
        } else {
            people.pop();
            answer++;
        }
    }
    
    return answer;
}
