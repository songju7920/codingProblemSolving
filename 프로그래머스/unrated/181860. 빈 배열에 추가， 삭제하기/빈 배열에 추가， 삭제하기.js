function solution(arr, flag) {
    let X = []; 
    
    flag.forEach((element, idx) => {
        if(element) for(let i = 0; i < arr[idx] * 2; i++) X.push(arr[idx]);
        else for(let i = 0; i < arr[idx]; i++) X.pop();
    });
    
    return X;
}