function solution(my_string) {
    return my_string.split('').map((element, idx) => {
        if(element === element.toUpperCase()){
            return element.toLowerCase();
        } else {
            return element.toUpperCase();
        }
    }).join('');
}