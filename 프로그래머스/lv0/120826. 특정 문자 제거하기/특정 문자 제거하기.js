function solution(my_string, letter) {
    let answer = '', cnt = 0;
    let characters = my_string.split("");
    characters.forEach(character => {
        if(character != letter[cnt]) answer += character;
    })
    return answer;
}