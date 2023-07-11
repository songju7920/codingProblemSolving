function solution(bridge_length, max_weight, truck_weights) {
    let onTheBridge = [];
    let exitBridgeTime = [];
    let weightSum = 0;
    let time = 1;
    truck_weights.reverse();
    
    while(onTheBridge.length > 0 || time == 1){
        //기존 트럭 처리
        if(exitBridgeTime[0] == time){
            weightSum -= onTheBridge.shift();
            exitBridgeTime.shift();
        }
        
        //새로운 트럭 처리
        let nextTruck = truck_weights.pop();
        
        if(weightSum + nextTruck <= max_weight){
            onTheBridge.push(nextTruck);
            weightSum += nextTruck;
            exitBridgeTime.push(bridge_length + time);
        } else {
            truck_weights.push(nextTruck);
        }
        
        time++;
    }
    
    return time - 1;
}