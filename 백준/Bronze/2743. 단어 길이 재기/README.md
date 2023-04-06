# [Bronze V] 단어 길이 재기 - 2743 

[문제 링크](https://www.acmicpc.net/problem/2743) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

구현, 문자열

### 문제 설명

<p>알파벳으로만 이루어진 단어를 입력받아, 그 길이를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어의 길이는 최대 100이다.</p>

### 출력 

 <p>첫째 줄에 입력으로 주어진 단어의 길이를 출력한다.</p>

---
풀이 코드:

```jsx
#include <stdio.h>

int main (void)
{
  char String[1000];
  int Cnt = 0;
  scanf("%s", String);
  for(int i = 0; String[i] != NULL; i++)
    Cnt++;
  printf("%d",Cnt);
}
```

나는 이 문제를 보고 반복문을 사용해서 풀었다. 하지만 사소한 경고나 문제점들을 방지하고, 최적화를 시킬수 있을 방법이 있었을 탠데 그걸 구현하지 못해 많이 아쉽다.

다른사람의 코드:

```jsx
int main(void){
    char input[100];
    scanf("%s", input);
    printf("%d\n",strlen(input));
}
```

위 코드에서는 반복문 대신 문자열의 길이를 측정 가능한 strlen이라는 함수를 사용하여 문제를 해결하였다.

- 알게된점
    
    strlen함수의 사용법및 활용
