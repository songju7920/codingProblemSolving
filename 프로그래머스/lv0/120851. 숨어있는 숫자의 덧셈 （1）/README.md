# [level 0] 숨어있는 숫자의 덧셈 (1) - 120851 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120851) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.11 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>문자열 <code>my_string</code>이 매개변수로 주어집니다. <code>my_string</code>안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>my_string</code>의 길이&nbsp;≤ 1,000</li>
<li><code>my_string</code>은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>my_string</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"aAb1B2cC34oOp"</td>
<td>10</td>
</tr>
<tr>
<td>"1a2b3c4d123"</td>
<td>16</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"aAb1B2cC34oOp"안의 한자리 자연수는 1, 2, 3, 4 입니다. 따라서 1 + 2 + 3 + 4 = 10 을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>"1a2b3c4d123Z"안의 한자리 자연수는 1, 2, 3, 4, 1, 2, 3 입니다. 따라서 1 + 2 + 3 + 4 + 1 + 2 + 3 = 16 을 return합니다.</li>
</ul>

<hr>

<h5>유의사항</h5>

<ul>
<li>연속된 숫자도 각각 한 자리 숫자로 취급합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

<p>
풀이 코드 분석 :
</p>
<pre>
    function solution(my_string) {
     var answer = 0; //answer 선언
     //my_string의 길이만큼 반복
     for(let i = 0; i < my_string.length; i++) 
         // my_string[i]가 NaN가 아닌가?
         if(isNaN(Number(my_string[i])) == false)
             //그렇다면 my_string[i]를 answer에 더하라
             answer += Number(my_string[i]);
     return answer; //answer 반환
     }
</pre>
처음에는 밑의 코드로 풀기를 시도했었다. 하지만 입력값에 포함되어있는 숫자는 문자열로 취급되기 때문에 (Ex : “D1D2D4”) 0이 출력되는 문제가 있었다.
<pre>
    function solution(my_string) {
        var answer = 0;
        for(let i = 0; i < my_string.length; i++)
            if(typeof my_string[i] == "Number")
                answer += my_string[i];
        return answer;
    }
</pre>
- 알게된점
    
    isNaN이라는 코드를 오늘 처음 알게되었다. isNaN은 is Not a Number의 약자로, 뒤에 위치한 어떤 값이 NaN인지 판별할때 쓴다. <br>
    
 <pre>      
    예제 코드 :   
    isNaN(123) => false //123은 숫자기 때문에 false가 출력된다.
    isNaN("0920") => false //문자열이지만 숫자로 취급하여 false가 출력된다.
    isNaN("") => false //빈 문자열은 0으로 취급한다.
    isNaN("123ABC") => true //문자가 포함되있어 NaN로 취급한다.
</pre>
