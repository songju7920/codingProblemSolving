#include <stdio.h>

int main() 
{
  int RepeatCnt, BoxCnt, ballChange1, ballChange2, save, BoxNum[100];
  scanf("%d %d", &BoxCnt, &RepeatCnt);
  for (int i = 1; i <= BoxCnt; i++) 
    BoxNum[i] = i;
  for (int i = 0; i < RepeatCnt; i++) 
  {
    scanf("%d %d", &ballChange1, &ballChange2);
    save = BoxNum[ballChange1];
    BoxNum[ballChange1] = BoxNum[ballChange2];
    BoxNum[ballChange2] = save;
  }
  for (int i = 1; i <= BoxCnt; i++) 
    printf("%d ", BoxNum[i]);
  return 0;
}