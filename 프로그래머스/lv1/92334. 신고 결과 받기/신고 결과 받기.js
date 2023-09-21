function solution(id_list, reports, k) {
    let answer = new Array(id_list.length).fill(0);
    let reportedCnts = new Array(id_list.length).fill(0);
    let bannedList = [];
    reports = [...new Set(reports)];
    
    reports.map(report => {
        let accused = report.split(" ")[1];
        reportedCnts[id_list.indexOf(accused)]++;
    })
    
    reportedCnts.map((reportedCnt, idx) => {
        if(reportedCnt >= k) bannedList.push(id_list[idx]);
    })
    
    reports.map(report => {
        let [reporter, reported] = report.split(" ");
        if(bannedList.indexOf(reported) != -1) {
            answer[id_list.indexOf(reporter)]++;
        }
    })
    
    return answer;
}