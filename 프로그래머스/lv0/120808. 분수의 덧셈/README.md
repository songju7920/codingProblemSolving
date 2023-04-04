# [level 0] 분수의 덧셈 - 120808 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120808#) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.22 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>첫 번째 분수의 분자와 분모를 뜻하는 <code>numer1</code>, <code>denom1</code>, 두 번째 분수의 분자와 분모를 뜻하는 <code>numer2</code>, <code>denom2</code>가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>0 &lt;<code>numer1</code>, <code>denom1</code>,&nbsp;<code>numer2</code>, <code>denom2</code> &lt; 1,000</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numer1</th>
<th>denom1</th>
<th>numer2</th>
<th>denom2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>[5, 4]</td>
</tr>
<tr>
<td>9</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>[29, 6]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
<hr>
<p>
풀이 코드 분석 :
</p>
<pre>
    function solution(numer1, denom1, numer2, denom2) {
    let topNum = numer1 * denom2 + numer2 * denom1; //분자 계산
    let bottomNum = denom1 * denom2; //분모 계산
    let max = 1; //max(최대공약수) 선언 및 초기화
    //bottomNum보다 작거나 같을동안 반복
    for(let i = 1; i <= bottomNum; i++)
    {
         //topNum / i가 나누어 떨어지고 bottomNum / i가 나누어 떨어지면
        if(topNum % i == 0 && bottomNum % i == 0) 
        max = i; //max에 i의 값 할당
    }
    return [topNum/max, bottomNum/max]; //[topNum/max, bottomNum/max] 리턴
}
</pre>
이 문제는 로직을 어떻게 상황에 맞게 출력할지 생각할때 많이 어려웠던 문제이다. 특히, 최대공약수를 구해 나눈다는 생각은 해냈지만 그걸 구현하는데에 많은 어려움이 있었다.<br/>

다른사람의 코드 :
<pre>
    function fnGCD(a, b){
        return (a%b)? fnGCD(b, a%b) : b;
    }

    function solution(denum1, num1, denum2, num2) {
        let denum = denum1*num2 + denum2*num1;
        let num = num1 * num2;
        let gcd = fnGCD(denum, num); //최대공약수

        return [denum/gcd, num/gcd];
    }
</pre>
위 코드는 함수를 따로 생성하여 코드의 가독성을 높이고 더 알아볼수 쉽게 구현하였다. 또한 재귀함수를 이용하여 반복문을 쓰지 않고 구현하였다.
