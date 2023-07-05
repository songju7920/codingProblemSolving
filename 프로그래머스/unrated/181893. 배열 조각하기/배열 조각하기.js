function solution(arr, query) {
    query.forEach((element, idx) => {
        if(idx % 2 == 0) arr.splice(element + 1, arr.length-element);
        else arr.splice(0, element);
    })
    
    return arr;
}