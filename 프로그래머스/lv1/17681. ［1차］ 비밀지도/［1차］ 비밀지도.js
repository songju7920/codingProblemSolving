function solution(n, arr1, arr2) {
    let MapData1 = [], MapData2 = [];
    let answer = [];
    
    //2진수 변환
    arr1.forEach(element => {
         MapData1.push(element.toString(2).padStart(n, "0"));
    })
    arr2.forEach(element => {
         MapData2.push(element.toString(2).padStart(n, "0"));
    })
    
    //지도 데이터 합치기
    for(let i = 0; i < n; i++){
        let Map = "";
        let Data1 = MapData1[i].split('');
        let Data2 = MapData2[i].split('');
        for(let j = 0; j < n; j++){
            if(Data1[j] == '1' || Data2[j] == '1') Map += '#';
            else Map += ' ';
        }
        answer.push(Map);
    }
    
    return answer;
}