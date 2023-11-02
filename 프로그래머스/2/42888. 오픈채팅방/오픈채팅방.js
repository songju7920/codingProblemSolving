function solution(records) {
    let hashTable = new Map();
    let result = [];
    
    // 최종 닉네임 도출
    records.map(record => {
        let [action, userID, nickname] = record.split(' ');
        
        if(!hashTable.has(userID)) {
            hashTable.set(userID, nickname);
        } else {
            if(action == 'Change') {
                hashTable.set(userID, nickname);
            } else if(action == 'Enter' && hashTable.get(userID) != nickname) {
                hashTable.set(userID, nickname);
            }
        }
    })
    
    // 메세지 생성
    records.map((record, idx) => {
        let [action, userID, nickname] = record.split(' ');
        nickname = hashTable.get(userID);
        if(action == "Enter") {
            result.push(`${nickname}님이 들어왔습니다.`);
        } else if (action == "Leave") {
            result.push(`${nickname}님이 나갔습니다.`);
        }
    })
    
    return result;
}