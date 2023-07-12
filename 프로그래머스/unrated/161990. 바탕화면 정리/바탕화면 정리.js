function solution(wallpaper) {
    let answer = [-1, -1, -1, -1];
    
    wallpaper.forEach((icon, idx) => {
        icon = icon.split('');
        let firstLocation = icon.indexOf('#');
        let lastLocation = icon.lastIndexOf('#') + 1;
        
        if(answer[0] == -1 && firstLocation != -1){
            answer[0] = idx;
            answer[1] = firstLocation;
        }
        if (lastLocation != 0) {
            answer[2] = idx + 1;
        }
        if(firstLocation < answer[1] && firstLocation != -1){
            answer[1] = firstLocation;
        } 
        if (lastLocation > answer[3]) {
            answer[3] = lastLocation;
        }
    })
    
    return answer;
}