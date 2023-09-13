function solution(today, terms, privacies) {
    var answer = [];
    
    let termObj = {}
    
    terms.map(term => {
        let [termName, termPeriod] = term.split(" ");
        termObj[`${termName}`] = Number(termPeriod);
    })

    privacies.map((privacy, idx) => {
        const [contractDate, term] = privacy.split(" ");
        
        //종료일 계산
        let [Cyear, Cmonth, Cdate] = contractDate.split(".");
        Cyear = Number(Cyear);
        Cmonth = Number(Cmonth);
        Cdate = Number(Cdate);
        
        Cmonth += termObj[term];
        while(Cmonth > 12) {
            Cyear += 1; 
            Cmonth -= 12;
        }
        
        //시간 비교
        let [Tyear, Tmonth, Tdate] = today.split(".");
        Tyear = Number(Tyear);
        Tmonth = Number(Tmonth);
        Tdate = Number(Tdate);
        
        if(Tyear > Cyear) answer.push(idx + 1);
        if (Tyear === Cyear && Tmonth > Cmonth) answer.push(idx + 1);
        if (Tyear === Cyear && Tmonth === Cmonth && Tdate >= Cdate) answer.push(idx + 1);
    })
    
    return answer;
}