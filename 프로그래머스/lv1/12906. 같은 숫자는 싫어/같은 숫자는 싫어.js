function solution(arr)
{
    var answer = [];
    let startPoint = 0;
    
    for(let i = 0; i < arr.length; i++){
        let Cnt = 0;
        for(let j = 1; j <= arr.length; j++)
            if(arr[startPoint] == arr[startPoint + j]) Cnt++;
            else if(arr[startPoint] != arr[startPoint + 1]){
                Cnt = 0;
                break;
            }
            else break;
        if(arr[startPoint] == null) break;
        answer[i] = arr[startPoint];
        startPoint += Cnt + 1;
    }
    
    return answer;
}