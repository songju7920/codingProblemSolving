#include <stdio.h>

int main (void)
{
  int subjectCnt, max = 0;
  double result;
  scanf("%d", &subjectCnt);
  int score[subjectCnt];
  for(int i = 0; i < subjectCnt; i++) {
      scanf("%d", &score[i]);
      if(score[i] > max)
        max = score[i];
    }
  for(int i = 0; i < subjectCnt; i++) {
      result += (double)score[i] / max * 100;
    }
  printf("%lf",result/subjectCnt);
}