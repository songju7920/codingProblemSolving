#include <stdio.h>

int main (void)
{
  int Cnt, repeat = 1;
  scanf("%d", &Cnt);
  for(int i = 1; i <= Cnt; i++)
    {
      for(int j = 0; j < Cnt - i; j++)
        printf(" ");
      for(int k = 0; k < repeat; k++)
        printf("*");
      printf("\n");
      repeat += 2;
    }
  repeat -= 2;
  for(int i = 1; i < Cnt; i++)
    {
      repeat -= 2;
      for(int j = 0; j < i; j++)
        printf(" ");
      for(int k = 0; k < repeat; k++)
        printf("*");
      printf("\n");
    }
}