function solution(n, losts, reserve) {
    let canAttend = n - losts.length;
    let length = losts.length;
    reserve.sort((a, b) => b - a)
    losts.sort((a, b) => a - b)
    
    //도난당한 학생이 여분이 있는 경우
    for(let i = 0; i < length; i++) {
        let lost = losts.shift();
        if(reserve.indexOf(lost) != -1) {
            reserve.splice(reserve.indexOf(lost), 1);
            canAttend++;
        } 
        else losts.push(lost);
    }
    
    //빌려주기
    while(losts.length > 0) {
        if(reserve.length < 1) break;
        let size = reserve.pop();
        for(let lost of losts) {
            if(Math.abs(lost - size) == 1){
                losts.splice(losts.indexOf(lost), 1);
                canAttend++;
            }
        }
    }
    
    return canAttend;
}