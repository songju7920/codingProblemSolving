function solution(arr, delete_list) {
    var answer = [];
    let location = 0;
    arr.forEach(element => {
        let Cnt = 0;
        for(let i = 0; i < delete_list.length; i++){
            if(element != delete_list[i]){
                Cnt++;
            }
        }
        if(Cnt > delete_list.length-1){
            answer[location] = element;
            location++;
        }
    })
    return answer;
}