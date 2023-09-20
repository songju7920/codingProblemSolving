function solution(babblings) {
    let answer = 0;
    babblings.map(babbling => {
        babbling = babbling.replaceAll(/aya(?!aya)|woo(?!woo)|ye(?!ye)|ma(?!ma)/g, '');
        if(babbling == '') answer++;
        console.log(babbling)
    })
    return answer;
}