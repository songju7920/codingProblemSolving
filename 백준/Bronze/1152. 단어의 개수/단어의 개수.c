#include <stdio.h>
#include <string.h>

int main (void)
{
  char String[1000000];
  int Cnt = 0;
  
  scanf("%[^\n]", String);

  for(int i = 1; i < strlen(String); i++)
      if(String[i] == ' ' && i != strlen(String) - 1)
        Cnt++;
  if(strlen(String) == 1 && String[0] == ' ')
    printf("0");
  else
    printf("%d", Cnt + 1);
}