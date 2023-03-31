function solution(sides) {
    var answer;
    if(sides[0] > sides[2] && sides[0] > sides[1])
        {
            if(sides[0] < sides[1] + sides[2])
                answer = 1;
            else
                answer = 2;
        }
    else if(sides[1] > sides[2] && sides[1] > sides[0])
        {
            if(sides[1] < sides[0] + sides[2])
                answer = 1;
            else
                answer = 2;
        }
        else
        {
            if(sides[2] < sides[0] + sides[1])
                answer = 1;
            else
                answer = 2;
        }
    return answer;
}