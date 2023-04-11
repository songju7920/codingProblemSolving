#include <stdio.h>

int main (void)
{
  int Cnt[6];
  for(int i = 0; i < 6; i++)
    scanf("%d", &Cnt[i]);
    printf("%d %d %d %d %d %d", 1 - Cnt[0], 1 - Cnt[1], 2 - Cnt[2], 2 - Cnt[3], 2 - Cnt[4], 8 - Cnt[5]);
}