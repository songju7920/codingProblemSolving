#include <stdio.h>
#include <string.h>

int main(void) {
  char Num[16];
  int sum = 0;

  scanf("%s",Num);
  
  for(int i = 0; i < strlen(Num); i++)
    {
      if(Num[i] < 68)
        sum += 3;
      else if(Num[i] < 71)
        sum += 4;
      else if(Num[i] < 74)
        sum += 5;
      else if(Num[i] < 77)
        sum += 6;
      else if(Num[i] < 80)
        sum += 7;
      else if(Num[i] < 84)
        sum += 8;
      else if(Num[i] < 87)
        sum += 9;
      else if(Num[i] < 91)
        sum += 10;
    }
  printf("%d", sum);
  return 0;
}