// cache using LRU = queue

function solution(cacheSize, cities) {
    let answer = 0;
    let cache = [];
    
    if(cacheSize != 0){
        cities.map(city => {
            city = city.toLowerCase();
            let cacheIdx = cache.indexOf(city);
            if(cacheIdx != -1) {
                cache.splice(cacheIdx, 1);
                cache.push(city);
                answer += 1;
            } else if (cache.length == cacheSize) {
                cache.shift();
                cache.push(city);
                answer += 5;
            } else {
                cache.push(city);
                answer += 5;
            }
        })
    } else {
        answer = cities.length * 5;
    }
    
    return answer;
}