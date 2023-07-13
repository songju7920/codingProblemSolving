#include <stdio.h>
#include <string.h>

int main() {
  int n;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    char answer1[55] = {0};
    char answer2[55] = {0};
    char str[27] = {0};
    int idx = 0;
    scanf("%s", str);

    for (int j = 0; j < strlen(str); j++) {
      answer1[idx] = str[j];
      j++;
      answer2[idx] = str[j];
      idx++;
    }
    idx--;

    if (strlen(str) % 2 != 0) {
      for (int j = 0; j < strlen(str); j++) {
        answer2[idx] = str[j];
        j++;
        idx++;
        answer1[idx] = str[j];
      }
    }

    printf("%s\n", answer1);
    printf("%s\n", answer2);
  }
}