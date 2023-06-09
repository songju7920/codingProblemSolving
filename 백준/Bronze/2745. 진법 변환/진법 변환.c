#include <stdio.h>
#include <string.h>

int main() {
  int n, sum = 0, square = 1, length = -1;
  char numbers[1000] = {-1};

  //입력받기
  for (int i = 0;; i++) {
    scanf("%c", &numbers[i]);
    if (numbers[i] == 32) {
      numbers[i] = -1;
      break;
    }
    if (numbers[i] > 64)
      numbers[i] -= 55;
    else
      numbers[i] -= 48;
    length++;
  }

  scanf("%d", &n);

  //계산
  for (int i = length; i > -1; i--) {
    sum += numbers[i] * square;
    square *= n;
  }
  printf("%d", sum);
}