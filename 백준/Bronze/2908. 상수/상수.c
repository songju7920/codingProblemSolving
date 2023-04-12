#include <stdio.h>

int main(void) {
  char Num1[4], Num2[4], greater[3];

  scanf("%s %s",Num1, Num2);

  for (int i = 2; i >= 0; i--)
    if (Num1[i] > Num2[i]) {
      for (int j = 2; j >= 0; j--)
        printf("%c", Num1[j]);
      break;
    } else if (Num1[i] < Num2[i]) {
      for (int j = 2; j >= 0; j--)
        printf("%c", Num2[j]);
      break;
    }
  return 0;
}