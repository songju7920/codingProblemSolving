#include <stdio.h>
#include <string.h>

int main() {
  int n;
  scanf("%d", &n);

  char console[51] = {0};
  char fileNames[50][51];
  for (int i = 0; i < n; i++) {
    scanf("%s", fileNames[i]);
  }

  for (int i = 0; i < strlen(fileNames[0]); i++) {
    int cnt = 0;

    for (int j = 1; j < n; j++) {
      if (fileNames[j-1][i] != fileNames[j][i]) {
        cnt++;
      }
    }

    if (cnt == 0) {
      console[i] = fileNames[0][i];
    } else {
      console[i] = '?';
    }
  }

  printf("%s", console);
}