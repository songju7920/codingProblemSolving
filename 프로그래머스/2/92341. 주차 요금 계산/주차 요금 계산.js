const calculateTime = (time1, time2) => {
    let [hour1, min1] = time1.split(':').map(a => Number(a));
    let [hour2, min2] = time2.split(':').map(a => Number(a));
    time1 = hour1 * 60 + min1;
    time2 = hour2 * 60 + min2;
    return time2 - time1;
}

function solution(fees, records) {
    let answer = [];
    let parkingLot = [];
    let enterTimes = [];
    let carNums = [...new Set(records.map(r => r.split(' ')[1]))].sort((a, b) => a - b);
    let totalTime =  new Array(carNums.length).fill(0);
    
    // 입출차 처리
    for(let record of records) {
        let [time, number, action] = record.split(' ');
        if(action === 'IN') {
            parkingLot.push(number);
            enterTimes.push(time);
        } else {
            let idx = parkingLot.indexOf(number);
            let enterTime = enterTimes[idx];
            parkingLot.splice(idx, 1);
            enterTimes.splice(idx, 1);
            totalTime[carNums.indexOf(number)] += calculateTime(enterTime, time);
        }
    }
    
    // 남아있는 차량 처리
    while(parkingLot.length > 0) {
        let idx = carNums.indexOf(parkingLot.pop());
        totalTime[idx] += calculateTime(enterTimes.pop(), "23:59");
    }
    
    // 요금 계산
    let [basicTime, basicFee, min ,feePerMin] = fees;
    for(let time of totalTime) {
        if(basicTime <= time) answer.push(basicFee + Math.ceil((time - basicTime) / min) * feePerMin);
        else answer.push(basicFee);
        
    }
    
    return answer;
}