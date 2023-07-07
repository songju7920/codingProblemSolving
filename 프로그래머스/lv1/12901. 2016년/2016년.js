function solution(a, b) {
    var days = 0;
    let weekData = [ "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
    
    //월 처리
    for(let i = 1; i < a; i++){
        if((i < 8 && i % 2 == 1) || (i > 7 && i % 2 == 0)) {
            days += 31;
        } else if(i == 2) { 
            days += 29;
        } else { 
            days += 30;
        }
    }
    
    days += b;
    
    //결과 출력
    return weekData[days % 7]
}