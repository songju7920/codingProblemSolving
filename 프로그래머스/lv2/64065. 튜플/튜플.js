function solution(tuple) {
    var answer = [];
    tuple = tuple.slice(2, tuple.length - 2)
                 .split(/},{/)
                 .sort((a, b) => a.length - b.length);
    
    tuple.map(arr => {
        arr = arr.split(',');
        arr.map(element => {
            if(answer.indexOf(element) == -1) answer.push(element)
        })
    })
    
    return answer.map(a => Number(a));
}