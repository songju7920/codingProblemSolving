#include <stdio.h>

int main (void)
{
  int Num, burlapBag = 0;
  scanf("%d", &Num);
  
  while(Num > 0) {
      if(Num >= 3 && Num % 5 != 0) {
          burlapBag++;
          Num -= 3;
          continue;
        }
      else if (Num >= 5) {
          burlapBag++;
          Num -= 5;
          continue;
      }
      else
        break;
    }
  
  if(Num == 0)
    printf("%d" , burlapBag);
  else 
    printf("-1"); 
}