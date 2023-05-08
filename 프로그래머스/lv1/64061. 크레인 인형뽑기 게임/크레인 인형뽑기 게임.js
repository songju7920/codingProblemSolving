function solution(board, moves) {
    var answer = 0;
    let basket = [];
    
    moves.forEach(move => {
        for(let i = 0; i < board.length; i++){
            const doll = board[i][move-1];
            if(doll === 0) continue;
            
            if(basket[basket.length-1] == doll){
                basket.pop();
                answer += 2;
            }
            
            else basket.push(doll);
            board[i][move-1] = 0;
            break;
        }
    })
    return answer;
}