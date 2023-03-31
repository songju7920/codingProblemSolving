#include <stdio.h>

int main(void) {
  int num, result[10], difResult = 0;
  for (int i = 0; i < 10; i++) {
    result[i] = -1;
  }
  for (int i = 0; i < 10; i++) {
    int count = 0;
    scanf("%d", &num);
    result[i] = num % 42;
    for (int j = 0; j < 10; j++) {
      if (result[i] == result[j])
        if (i != j) count++;
    }
    if (count == 0)
      difResult++;
  }
  printf("%d\n", difResult);
}