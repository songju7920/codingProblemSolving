const manhattanDistance = (location1, location2) => {
  let x = Math.abs(location1[0] - location2[0]);
  let y = Math.abs(location1[1] - location2[1]);

  return x+y;
}

function solution(numbers, hand) {
    var answer = '';
    let leftHand = [3, 0], rightHand = [3, 2];
    let keyPad = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]];
    numbers.map(number => {
        if(number % 3 == 1){
            leftHand = keyPad[number];
            answer += "L";
        } else if(number % 3 == 0 && number != 0) {
            rightHand = keyPad[number];
            answer += "R";
        } else {
            let disL = manhattanDistance(leftHand, keyPad[number]);
            let disR = manhattanDistance(rightHand, keyPad[number]);
            
            if(disL > disR || disL == disR && hand == 'right') {
                rightHand = keyPad[number];
                answer += "R";
            } else {
                leftHand = keyPad[number];
                answer += "L";
            }
        }
    })
    return answer;
}