function solution(strArr) {
    return strArr.filter(str => str.match(/ad/g) == null);
}