#include <stdio.h>

int main(void) {
  int A, B, V, Day;
  scanf("%d %d %d", &A, &B, &V);
  Day = (V-B-1)/(A-B)+1;
  printf("%d",Day);
}