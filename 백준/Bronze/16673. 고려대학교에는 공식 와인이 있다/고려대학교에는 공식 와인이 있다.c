#include <stdio.h>

int main(void) {
  int K;
  int P;
  int C;
  int total = 0;

  scanf("%d %d %d", &C, &K, &P);

  for (int i = 1; i <= C; i++) {
    total += K * i + P * i * i;
  }

  printf("%d", total);
}