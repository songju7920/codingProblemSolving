#include <stdio.h>
#include <stdlib.h>

int main (void)
{
  int Cnt, result = 0;
  scanf("%d", &Cnt);
  char Num[Cnt];
  scanf("%s", Num);
  for(int i = 0; i < Cnt; i++)
    {
      result += (int)(Num[i]) - 48;
    }
  printf("%d",result);
}