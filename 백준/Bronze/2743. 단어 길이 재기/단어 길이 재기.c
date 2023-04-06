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