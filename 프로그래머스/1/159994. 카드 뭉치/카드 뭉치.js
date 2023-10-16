function solution(cards1, cards2, goal) {
    for(let idx in goal) {
        if(cards1[0] == goal[idx]) cards1.shift();
        else if(cards2[0] == goal[idx]) cards2.shift();
        else return 'No'
    }
    return 'Yes';
}