function solution(new_id) {
    var answer = '';
    new_id = new_id.toLowerCase()
    .replaceAll(/[^\w\-\.]/g, "")
    .replaceAll(/\.{2,}/g, ".")
    .replace(/\.$/, "")
    .replace(/^\./, "");
    
    new_id = new_id == "" ? "a" : new_id;
    new_id = new_id.split('').splice(0, 15).reduce((a, b) => a + b).replace(/\.$/, "");
    while(new_id.length < 3) new_id += new_id[new_id.length - 1];
    return new_id;
}