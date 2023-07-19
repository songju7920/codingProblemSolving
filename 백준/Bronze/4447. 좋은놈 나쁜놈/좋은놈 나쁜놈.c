#include <stdio.h>
#include <string.h>

int main() {
  int n;
  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    char name[26] = {0};
    scanf(" %[^\n]", name);
    getchar();
    int gCnt = 0, bCnt = 0;

    for (int j = 0; j < strlen(name); j++) {
      if (name[j] == 'g' || name[j] == 'G') {
        gCnt++;
      } else if (name[j] == 'b' || name[j] == 'B') {
        bCnt++;
      }
    }

    if (gCnt > bCnt) {
      printf("%s is GOOD\n", name);
    } else if (gCnt < bCnt) {
      printf("%s is A BADDY\n", name);
    } else {
      printf("%s is NEUTRAL\n", name);
    }
  }
}