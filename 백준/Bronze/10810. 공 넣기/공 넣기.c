#include <stdio.h>

int main() 
{
  int RepeatCnt, BoxCnt, putInBallStart, putInBallEnd, putInBallNum;
  scanf("%d %d", &BoxCnt, &RepeatCnt);
  int BoxNum[BoxCnt];
  for (int i = 1; i <= BoxCnt; i++) 
    BoxNum[i] = 0;
  for (int i = 1; i <= RepeatCnt; i++) 
  {
    scanf("%d %d %d", &putInBallStart, &putInBallEnd, &putInBallNum);
    for (; putInBallStart <= putInBallEnd; putInBallStart++) 
      BoxNum[putInBallStart] = putInBallNum;
  }
  for (int i = 1; i <= BoxCnt; i++) 
  {
    printf("%d ", BoxNum[i]);
  }
  return 0;
}