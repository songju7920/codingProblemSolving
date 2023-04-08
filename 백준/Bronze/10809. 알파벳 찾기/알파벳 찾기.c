#include <stdio.h>
#include <string.h>

int main (void)
{
  char String[100];
  int location[100];
  
  for(int i = 0; i < 100; i++)
    location[i] = -1;
  
  scanf("%s", String);
  for(int a = 97; a < 123; a++)
    for(int i = 0; i < strlen(String); i++)
      if (String[i] == (char)a)
      {
        location[a - 97] = i;
        break;
      }
  
  for(int i = 0; i < 26; i++)
    printf("%d ",location[i]);
}