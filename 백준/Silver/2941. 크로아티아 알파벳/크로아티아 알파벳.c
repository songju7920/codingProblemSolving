#include <stdio.h>
#include <string.h>

int main(void) {
  char str[101];
  int Cnt = 0;
  scanf("%s", str);
  
  for(int i = 0; i < strlen(str); i++)
   if(str[i+1] == '=' || str[i+1] == '-'){
     Cnt++;
     i++;
   }
   else if((str[i] == 'l' || str[i] == 'n')&& str[i+1] == 'j'){
     Cnt++;
     i++;
   }
   else if(str[i] == 'd' && str[i+1] == 'z' && str[i+2] == '='){
     Cnt++;
     i += 2;
   }
   else
     Cnt++;
  printf("%d",Cnt);
  return 0;
}