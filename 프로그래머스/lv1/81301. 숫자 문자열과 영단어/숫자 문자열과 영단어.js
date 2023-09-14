const numbers = {
    zero: 0,  five: 5,
    one: 1,   six: 6,
    two: 2,   seven: 7,
    three: 3, eight: 8,
    four: 4,  nine: 9,
}

function solution(s) {
    let numArr = ["zero", "one", "two", "three", "four", 
                  "five", "six", "seven", "eight", "nine"];
    
    numArr.map(num => {
        let regexp = new RegExp(`${num}`, 'g');
        s = s.replaceAll(regexp, numbers[`${num}`]);
        console.log(s);
    });
    
    return Number(s);
}