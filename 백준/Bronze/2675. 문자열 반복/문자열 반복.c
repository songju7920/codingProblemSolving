#include <stdio.h>
#include <string.h>

int main (void)
{
  char String[20];
  int Cnt, repeat;
  
  scanf("%d", &Cnt);

  for(int i = 0; i < Cnt; i++)
    {
      scanf("%d", &repeat);
      scanf("%s", String);
      for(int x = 0; x < strlen(String); x++)
        for(int j = 0; j < repeat; j++)
          printf("%c", String[x]);
      printf("\n");
    }
}